using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;

namespace Baekjoon
{
    class Program
    {
        static void Main(string[] args)
        {
            StreamReader inp = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
            StreamWriter outp = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
            StringBuilder sb = new StringBuilder();

            int n = int.Parse(inp.ReadLine());

            if (n > 10000) {
                sb.AppendLine("Time limit exceeded");            
            } else {
                sb.AppendLine("Accepted");
            }

            outp.Write(sb);
            outp.Close();
            inp.Close();
        }
    }
}

// 제출 번호 : 102171180, 메모리 : 5504, 시간 : 44