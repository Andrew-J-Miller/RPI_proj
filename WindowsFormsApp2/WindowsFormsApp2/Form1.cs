using System;
using System.Windows.Forms;
using System.Threading;
using System.Diagnostics;
//using Microsoft.Scripting.Hosting;


namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {

    public Form1()
        {

            InitializeComponent();
            // PythonEngine.Initialize();
                    


        }

        //varibale
        int hours, minutes, seconds;
        
        //Close the application
        private void ExistButton_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("Do you want to close the process?", "Exit", MessageBoxButtons.YesNo)
                == DialogResult.Yes)
                this.Close();
        }

        //This function will allow the user to reset the appliction and restart again
        private void ResetButton_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Clear();
            FahrenheitRadio.Checked = false;
            CelsiusRadio.Checked = false;
            HourNumeric1.Value = 0;
            HourNumeric2.Value = 0;
            HourNumeric3.Value = 0;
            MinuteNumeric1.Value = 0;
            Minuteumeric2.Value = 0;
            MinuteNumeric3.Value = 0;
            SecondNumeric1.Value = 0;
            SecondNumeric2.Value = 0;
            SecondNumeric3.Value = 0;
            HoursLabel1.Text = "";
            HourLabel2.Text = "";
            HourLabel3.Text = "";
            MinutesLabel1.Text = "";
            MinuteLabel2.Text = "";
            MinuteLabel3.Text = "";
            SecondsLabel1.Text = "";
            SecondLabel2.Text = "";
            SecondLabel3.Text = "";
        }
 
 

        private void About_Click(object sender, EventArgs e)
        {
            AboutBox1 a = new AboutBox1();
            a.ShowDialog();
        }

        private void HelpButton_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("Contact us:" +"  "+
                "800-443-5555" +"  " +
                "brewersystem@brewordie.com", "Exit", MessageBoxButtons.OK)
                 == DialogResult.Yes)
                this.Close();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        int hours2, minutes2, seconds2;
        private void timer2_Tick(object sender, EventArgs e)
        {
            if (hours2 == 0 && minutes2 == 0 && seconds2 == 0)// on here we chack if the time is up and we add some stuff on times up
            {
                timer1.Stop();
                //MessageBox.Show(new Form() { TopMost = true }, "Times up!!! :P", "Will you press OK? :P", MessageBoxButtons.OK, MessageBoxIcon.Information);
                HourNumeric2.Text = "00";
                Minuteumeric2.Text = "00";
                SecondNumeric2.Text = "00";
                SecondNumeric2.Enabled = true;
                Minuteumeric2.Enabled = true;
                HourNumeric2.Enabled = true;
                StartButton2.Enabled = true;
                HourLabel2.Text = "00";
                MinuteLabel2.Text = "00";
                SecondLabel2.Text = "00";
            }
            else
            {
                if (seconds2 < 1)// here is the most important code (dont forget to change the timer to 1000 milliseconds)!!! first we check if the secs are smaller than 1
                {
                    seconds2 = 59;// on here we make the secs to 59 if it is smaller than 1
                    if (minutes2 < 1)// here we check if the minutes are smaller than 1
                    {
                        minutes2 = 59;// on here we make the mins to 59 if it is smaller than 1
                        if (hours2 != 0)// on here we check if the hours are different from 0
                            hours2 -= 1;// on here we remove from the current hour the number 1. its the same if we write hours = hours - 1;
                    }
                    else minutes2 -= 1;// on here we remove fro mthe current mins 1

                }
                else seconds2 -= 1;// and here we do the same with the seconds
                if (hours2 > 9)// and on this stage we add the numbers on the labels
                    HourLabel2.Text = hours2.ToString();
                else HourLabel2.Text = "0" + hours2.ToString();
                if (minutes2 > 9)
                    MinuteLabel2.Text = minutes2.ToString();
                else MinuteLabel2.Text = "0" + minutes2.ToString();
                if (seconds2 > 9)
                    SecondLabel2.Text = seconds2.ToString();
                else SecondLabel2.Text = "0" + seconds2.ToString();
            }
        }

        int hours3, minutes3, seconds3;
        private void timer3_Tick(object sender, EventArgs e)
        {
            if (hours3 == 0 && minutes3 == 0 && seconds3 == 0)// on here we chack if the time is up and we add some stuff on times up
            {
                timer1.Stop();
                //MessageBox.Show(new Form() { TopMost = true }, "Times up!!! :P", "Will you press OK? :P", MessageBoxButtons.OK, MessageBoxIcon.Information);
                HourNumeric3.Text = "00";
                MinuteNumeric3.Text = "00";
                SecondNumeric3.Text = "00";
                SecondNumeric3.Enabled = true;
                MinuteNumeric3.Enabled = true;
                HourNumeric3.Enabled = true;
                StartButton3.Enabled = true;
                HourLabel3.Text = "00";
                MinuteLabel3.Text = "00";
                SecondLabel3.Text = "00";
            }
            else
            {
                if (seconds3 < 1)// here is the most important code (dont forget to change the timer to 1000 milliseconds)!!! first we check if the secs are smaller than 1
                {
                    seconds3 = 59;// on here we make the secs to 59 if it is smaller than 1
                    if (minutes3 < 1)// here we check if the minutes are smaller than 1
                    {
                        minutes3 = 59;// on here we make the mins to 59 if it is smaller than 1
                        if (hours3 != 0)// on here we check if the hours are different from 0
                            hours3 -= 1;// on here we remove from the current hour the number 1. its the same if we write hours = hours - 1;
                    }
                    else minutes3 -= 1;// on here we remove fro mthe current mins 1

                }
                else seconds3 -= 1;// and here we do the same with the seconds
                if (hours3 > 9)// and on this stage we add the numbers on the labels
                    HourLabel3.Text = hours3.ToString();
                else HourLabel3.Text = "0" + hours3.ToString();
                if (minutes3 > 9)
                    MinuteLabel3.Text = minutes3.ToString();
                else MinuteLabel3.Text = "0" + minutes3.ToString();
                if (seconds3 > 9)
                    SecondLabel3.Text = seconds3.ToString();
                else SecondLabel3.Text = "0" + seconds3.ToString();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Stop();
            timer2.Stop();
            timer3.Stop();
        }

        private void number1_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Text +="1";
        }



        private void HourNumeric1_ValueChanged(object sender, EventArgs e)
        {
            HourNumeric1.Maximum = 24;
            HourNumeric1.Minimum = 0;
        }

        private void MinuteNumeric1_ValueChanged(object sender, EventArgs e)
        {
            MinuteNumeric1.Maximum = 59;
            MinuteNumeric1.Minimum = 0;
        }

        private void SecondNumeric1_ValueChanged(object sender, EventArgs e)
        {
            SecondNumeric1.Maximum = 60;
            SecondNumeric1.Minimum = 0;
        }

        private void HourNumeric2_ValueChanged(object sender, EventArgs e)
        {
            HourNumeric2.Maximum = 24;
            HourNumeric2.Minimum = 0;
        }

        private void Minuteumeric2_ValueChanged(object sender, EventArgs e)
        {
            Minuteumeric2.Maximum = 59;
            Minuteumeric2.Minimum = 0;
        }

        private void SecondNumeric2_ValueChanged(object sender, EventArgs e)
        {
            SecondNumeric2.Maximum = 60;
            SecondNumeric2.Minimum = 0;
        }

        private void HourNumeric3_ValueChanged(object sender, EventArgs e)
        {
            HourNumeric3.Maximum = 24;
            HourNumeric3.Minimum = 0;
        }

        private void MinuteNumeric3_ValueChanged(object sender, EventArgs e)
        {
            MinuteNumeric3.Maximum = 59;
            MinuteNumeric3.Minimum = 0;
        }

        private void SecondNumeric3_ValueChanged(object sender, EventArgs e)
        {
            SecondNumeric3.Maximum = 60;
            SecondNumeric3.Minimum = 0;
        }

        private void number2_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Text += "2";
        }

        private void number3_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Text += "3";
        }

        private void number4_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Text += "4";
        }

        private void number5_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Text += "5";
        }

        private void number6_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Text += "6";
        }

        private void number7_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Text += "7";
        }

        private void StartButton2_Click(object sender, EventArgs e)
        {
            if (HourNumeric2.Text == "" || Minuteumeric2.Text == "" || SecondNumeric2.Text == "")//here we check if the textboxes are empty
            {
                MessageBox.Show("No correct inputs");
            }
            else// on here we save the textboxes values to some variables named hours, mins, secs and we start the timer
            {
                hours2 = int.Parse(HourNumeric2.Text);
                minutes2 = int.Parse(Minuteumeric2.Text);
                seconds2 = int.Parse(SecondNumeric2.Text);
                HourNumeric2.Enabled = true;
                Minuteumeric2.Enabled = true;
                SecondNumeric2.Enabled = true;
                StartButton2.Enabled = true;
                timer2.Start();
            }
        }

        private void StartButton3_Click(object sender, EventArgs e)
        {
            if (HourNumeric3.Text == "" || MinuteNumeric3.Text == "" || SecondNumeric3.Text == "")//here we check if the textboxes are empty
            {
                MessageBox.Show("No correct inputs");
            }
            else// on here we save the textboxes values to some variables named hours, mins, secs and we start the timer
            {
                hours3 = int.Parse(HourNumeric3.Text);
                minutes3 = int.Parse(MinuteNumeric3.Text);
                seconds3 = int.Parse(SecondNumeric3.Text);
                HourNumeric3.Enabled = true;
                MinuteNumeric3.Enabled = true;
                SecondNumeric3.Enabled = true;
                StartButton3.Enabled = true;
                timer3.Start();
            }
        }

        private void StartButton1_Click(object sender, EventArgs e)
        {
            if (HourNumeric1.Text == "" || MinuteNumeric1.Text == "" || SecondNumeric1.Text == "")//here we check if the textboxes are empty
            {
                MessageBox.Show("No correct inputs");
            }
            else// on here we save the textboxes values to some variables named hours, mins, secs and we start the timer
            {
                hours = int.Parse(HourNumeric1.Text);
                minutes = int.Parse(MinuteNumeric1.Text);
                seconds = int.Parse(SecondNumeric1.Text);
                HourNumeric1.Enabled = true;
                MinuteNumeric1.Enabled = true;
                SecondNumeric1.Enabled = true;
                StartButton1.Enabled = true;
                timer1.Start();
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            run_cooling();
        }

        private void run_cooling()
        {
            string cool = @"C:\CoolScript.py";
            Process c = new Process();
            c.StartInfo = new ProcessStartInfo(@"C:\Python34\python.exe", cool)
            {
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };
            c.Start();

            string output = c.StandardOutput.ReadToEnd();
            c.WaitForExit();

            Console.WriteLine(output);

            Console.ReadLine();
        }


        private void NumberOfDegree_TextChanged(object sender, EventArgs e)
        {

        }

        private void EStopButton_Click(object sender, EventArgs e)
        {
            //To stop all process
            Process[] myProcesses;

            // Returns array containing all instances of Notepad.
            myProcesses = Process.GetProcessesByName("Notepad");
            foreach (Process myProcess in myProcesses)
            {
                if (myProcess.Responding)
                {
                    myProcess.CloseMainWindow();
                }
                else
                {
                    myProcess.Kill();
                }
            }
        }

        private void BoilingButton_Click(object sender, EventArgs e)
        {
            run_boiling();
        }

        private void run_boiling()
        {
            string boil = @"C:\BoilScript.py";
            Process b = new Process();
            b.StartInfo = new ProcessStartInfo(@"C:\Python34\python.exe", boil)
            {
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };
            b.Start();

            string output = b.StandardOutput.ReadToEnd();
            b.WaitForExit();

            Console.WriteLine(output);

            Console.ReadLine();
        }

        private void MashingButton_Click(object sender, EventArgs e)
        {
            run_mashing();
        }

        private void run_mashing()
        {
            string mash = @"C:\MashScript.py";
            Process m = new Process();
            m.StartInfo = new ProcessStartInfo(@"C:\Python34\python.exe", mash)
            {
                RedirectStandardOutput = true,
                UseShellExecute = false,
                CreateNoWindow = true
            };
            m.Start();

            string output = m.StandardOutput.ReadToEnd();
            m.WaitForExit();

            Console.WriteLine(output);

            Console.ReadLine();
        }
        
        private void CurrentTemperature_Click(object sender, EventArgs e)
        {
            run_current_temperature();
        }

        private void run_current_temperature()
        {
            string curtemp = @"C:\HeaterTemplate.py";
            Process temp = new Process();
            temp.StartInfo = new ProcessStartInfo(@"C:\Python34\python.exe", curtemp)
            {
            RedirectStandardOutput = true,
            UseShellExecute = false,
            CreateNoWindow = true,
            };
            temp.Start();

            string output = temp.StandardOutput.ReadToEnd();
            temp.WaitForExit();

            Console.WriteLine(output);

            Console.ReadLine();
        }

        private void number8_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Text += "8";
        }

        private void number9_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Text += "9";
        }

        private void number0_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Text += "0";
        }

        private void delete_Click(object sender, EventArgs e)
        {
            NumberOfDegree.Text = "";
        }


        //The user touch the text box and a numeric keypad will display
        private void NumberOfDegree_KeyPress_1(object sender, KeyPressEventArgs e)
        {
            //Ignore if not 0-9 or backspace char
            if ((e.KeyChar < '0' || e.KeyChar > '9') && (e.KeyChar != '\b'))
            {
                e.Handled = true;
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (hours == 0 && minutes == 0 && seconds == 0)// on here we chack if the time is up and we add some stuff on times up
            {
                timer1.Stop();
                //MessageBox.Show(new Form() { TopMost = true }, "Times up!!! :P", "Will you press OK? :P", MessageBoxButtons.OK, MessageBoxIcon.Information);
                HourNumeric1.Text = "00";
                MinuteNumeric1.Text = "00";
                SecondNumeric1.Text = "00";
                SecondNumeric1.Enabled = true;
                MinuteNumeric1.Enabled = true;
                HourNumeric1.Enabled = true;
                StartButton1.Enabled = true;
                HoursLabel1.Text = "00";
                MinutesLabel1.Text = "00";
                SecondsLabel1.Text = "00";
            }
            else
            {
                if (seconds < 1)// here is the most important code (dont forget to change the timer to 1000 milliseconds)!!! first we check if the secs are smaller than 1
                {
                    seconds = 59;// on here we make the secs to 59 if it is smaller than 1
                    if (minutes < 1)// here we check if the minutes are smaller than 1
                    {
                        minutes = 59;// on here we make the mins to 59 if it is smaller than 1
                        if (hours != 0)// on here we check if the hours are different from 0
                            hours -= 1;// on here we remove from the current hour the number 1. its the same if we write hours = hours - 1;
                    }
                    else minutes -= 1;// on here we remove fro mthe current mins 1

                }
                else seconds -= 1;// and here we do the same with the seconds
                if (hours > 9)// and on this stage we add the numbers on the labels
                    HoursLabel1.Text = hours.ToString();
                else HoursLabel1.Text = "0" + hours.ToString();
                if (minutes > 9)
                    MinutesLabel1.Text = minutes.ToString();
                else MinutesLabel1.Text = "0" + minutes.ToString();
                if (seconds > 9)
                    SecondsLabel1.Text = seconds.ToString();
                else SecondsLabel1.Text = "0" + seconds.ToString();
            }
        }
    }
}
