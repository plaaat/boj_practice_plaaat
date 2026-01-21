using System;
using System.Text;
using System.Linq;
using System.Collections.Generic;
using System.Numerics;

namespace Baekjoon
{
    class Program
    {
        static void Main(string[] args)
        {
            StreamReader inp = new StreamReader(new BufferedStream(Console.OpenStandardInput()));
            StreamWriter outp = new StreamWriter(new BufferedStream(Console.OpenStandardOutput()));
            StringBuilder sb = new StringBuilder();

            string[] inp1 = inp.ReadLine()!.Split();
            int n = int.Parse(inp1[0]);
            long t = long.Parse(inp1[1]);
            long idx = (t - 1) % (4 * n - 2);

            if (idx < 2 * n)
            {
                sb.AppendLine((idx+1).ToString());
            } else
            {
                sb.AppendLine((4 * n - 1 - idx).ToString());
            }

            outp.Write(sb);
            outp.Close();
            inp.Close();
        }
    }
}

// 제출 번호 : 102172543, 메모리 : 5512, 시간 : 48