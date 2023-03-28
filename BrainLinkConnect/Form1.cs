using System;
using System.Collections.Generic;
//using System.ComponentModel;
using System.Data;
using System.Diagnostics;
//using System.Drawing;
using System.Linq;
using System.Text;
//using System.Threading.Tasks;
using System.Windows.Forms;
//using System.Windows.Forms.DataVisualization.Charting;
//using static BrainLinkSDK_Windows.BrainLinkSDK;
//using System.Threading;
using System.IO;
//using System.Reflection;
//using System.Windows.Forms.VisualStyles;

namespace BrainLinkConnect
{
    public partial class Form1 : Form
    {
        private BrainLinkSDK_Windows.BrainLinkSDK brainLinkSDK;
        
        public static DataTable table = new DataTable();
        
        public static string timeStamp;
        
        public static string fileName;

        private float ave = 0;

        private List<int> raw = new List<int>();

        private List<float> hrvList = new List<float>();

        private List<double> lastHRV = new List<double>();

        private List<(long, string)> Devices = new List<(long, string)>();


        // Time stamp function 
        public static string GetTimestamp(DateTime value, bool name = false)
        {
            if (name)
                return value.ToString("dd-MM-yyyy_HHmm");
            // return value.ToString("yyyyMMddHHmmssffff");
            return value.ToString("dd-MM-yyyy_HH:mm:ss");
        }

        // Datatable creation 
        public static void createDataTableHeader()
        {
            //columns  
            table.Columns.Add("Timestamp", typeof(string));
            table.Columns.Add("Attention", typeof(string));
            table.Columns.Add("Meditation", typeof(string));
            table.Columns.Add("Delta", typeof(string));
            table.Columns.Add("Theta", typeof(string));
            table.Columns.Add("LowAlpha", typeof(string));
            table.Columns.Add("HighAlpha", typeof(string));
            table.Columns.Add("LowBeta", typeof(string));
            table.Columns.Add("HighBeta", typeof(string));
            table.Columns.Add("LowGamma", typeof(string));
            table.Columns.Add("HighGamma", typeof(string));
        }

        public static void exportDataTableToCSV(DataTable dt)
        {
            StringBuilder sb = new StringBuilder();
            IEnumerable<string> columnNames = dt.Columns.Cast<DataColumn>().
                                            Select(column => column.ColumnName);
            sb.AppendLine(string.Join(",", columnNames));

            foreach (DataRow row in dt.Rows)
            {
                IEnumerable<string> fields = row.ItemArray.Select(field => field.ToString());
                sb.AppendLine(string.Join(",", fields));
            }

            //File.WriteAllText(fileName.ToString() + ".csv", sb.ToString());
            try {

                File.WriteAllText(fileName+"test.csv", sb.ToString());
            }
            catch (IOException e)
            {
                Debug.WriteLine(e.ToString());
            }
        }

        public Form1()
        {
            InitializeComponent();
            createDataTableHeader();
            fileName = GetTimestamp(DateTime.Now, true);
            brainLinkSDK = new BrainLinkSDK_Windows.BrainLinkSDK();
            brainLinkSDK.OnEEGDataEvent += new BrainLinkSDK_Windows.BrainLinkSDKEEGDataEvent(BrainLinkSDK_OnEEGDataEvent);
            brainLinkSDK.OnEEGExtendEvent += new BrainLinkSDK_Windows.BrainLinkSDKEEGExtendDataEvent(BrainLinkSDK_OnEEGExtendDataEvent);
            brainLinkSDK.OnGyroDataEvent += new BrainLinkSDK_Windows.BrainLinkSDKGyroDataEvent(BrainLinkSDK_OnGyroDataEvent);
            brainLinkSDK.OnHRVDataEvent += new BrainLinkSDK_Windows.BrainLinkSDKHRVDataEvent(BrainLinkSDK_OnHRVDataEvent);
            brainLinkSDK.OnRawDataEvent += new BrainLinkSDK_Windows.BrainLinkSDKRawDataEvent(BrainLinkSDK_OnRawDataEvent);
            brainLinkSDK.OnDeviceFound += new BrainLinkSDK_Windows.BrainLinkSDKOnDeviceFoundEvent(BrainLinkSDK_OnDeviceFoundEvent);
        }

        private void BrainLinkSDK_OnDeviceFoundEvent(long Address, string Name)
        {
            Debug.WriteLine("Discover name " + Name);
            listBox1.Items.Add(Name + " : " + Address.ToString("X12"));
            Devices.Add((Address, Name));
        }

        private void BrainLinkSDK_OnRawDataEvent(int Raw)
        {
            raw.Add(Raw);
            if (raw.Count > 512)
            {
                raw.Remove(raw[0]);
            }
            chart1.Series[0].Points.DataBindY(raw);
        }

        private void BrainLinkSDK_OnHRVDataEvent(int[] HRV, int Blink)
        {
            for (int i = 0; i < HRV.Length; i++)
            {
                hrvBox.Text += HRV[i] + "ms ";
                hrvList.Add(HRV[i]);
            }
            if (hrvList.Count >= 60)
            {
                double hrv = StandardDiviation(hrvList.ToArray());
                lastHRV.Add(hrv);
                if (lastHRV.Count > 5)
                {
                    lastHRV.RemoveAt(0);
                }
                string hrvString = "";
                for (int i = 0; i < lastHRV.Count; i++)
                {
                    hrvString += "hrv" + i + ":" + lastHRV[i].ToString("F2");
                }
                hrvString += " avg:" + ave.ToString("F2") + " size:" + hrvList.Count;
                hrvList.Clear();
                hrvLabel.Text = hrvString;
                hrvBox.Text = "";
            }
        }

        private void BrainLinkSDK_OnGyroDataEvent(int X, int Y, int Z)
        {
            xvalue.Text = X.ToString();
            yvalue.Text = Y.ToString();
            zvalue.Text = Z.ToString();
        }

        private void BrainLinkSDK_OnEEGExtendDataEvent(BrainLinkSDK_Windows.BrainLinkExtendModel Model)
        {
            //Debug.WriteLine("Extend");
            ap.Text = Model.Ap.ToString();
            ele.Text = Model.Electric.ToString();
            version.Text = Model.Version.ToString();
            temp.Text = Model.Temperature.ToString();
            heart.Text = Model.HeartRate.ToString();
        }

        private void Start_Click(object sender, EventArgs e)
        {
            Debug.WriteLine("Click");
            brainLinkSDK.Start();
            listBox1.Items.Clear();
            Devices.Clear();
        }

        private void BrainLinkSDK_OnEEGDataEvent(BrainLinkSDK_Windows.BrainLinkModel Model)
        {
            att.Text = Model.Attention.ToString();
            med.Text = Model.Meditation.ToString();
            delta.Text = Model.Delta.ToString();
            theta.Text = Model.Theta.ToString();
            lalpha.Text = Model.LowAlpha.ToString();
            halpha.Text = Model.HighAlpha.ToString();
            lbeta.Text = Model.LowBeta.ToString();
            hbeta.Text = Model.HighBeta.ToString();
            lgamma.Text = Model.LowGamma.ToString();
            hgamma.Text = Model.HighGamma.ToString();
            signal.Text = Model.Signal.ToString();

            //adding values to DataTable
            timeStamp = GetTimestamp(DateTime.Now);
            table.Rows.Add(timeStamp, att.Text, med.Text, delta.Text, theta.Text,
                lalpha.Text, halpha.Text, lbeta.Text, hbeta.Text, lgamma.Text, hgamma.Text);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //Debug.WriteLine("Click");
            //brainLinkSDK.Start();
        }

        private double StandardDiviation(float[] x)
        {
            ave = x.Average();
            double dVar = 0;
            for (int i = 0; i < x.Length; i++)
            {
                dVar += (x[i] - ave) * (x[i] - ave);
            }
            return Math.Sqrt(dVar / x.Length);
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            brainLinkSDK.SetApEnable(checkBox1.Checked);
        }

        private void checkBox2_CheckedChanged(object sender, EventArgs e)
        {
            brainLinkSDK.SetGyroEnable(checkBox2.Checked);
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (brainLinkSDK != null)
            { 
                brainLinkSDK.Close();
                brainLinkSDK = null;
                exportDataTableToCSV(table);
            }
            Dispose();
            Application.Exit();
        }

        private void Form1_Shown(object sender, EventArgs e)
        {

        }

        private void Connect_Click(object sender, EventArgs e)
        {
            if (listBox1.Items.Count > 0 && listBox1.SelectedIndex < Devices.Count)
            {
                (long, string) Device = Devices[listBox1.SelectedIndex];
                brainLinkSDK.connect(Device.Item1);
            }
        }

        private void Stop_Click(object sender, EventArgs e)
        {
            exportDataTableToCSV(table);
            listBox1.Items.Clear();
            Devices.Clear();
        }

    }
}
