import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
import unittest
from arrays_strings.unique_email import UniqueEmail

class TestUniqueEmail(unittest.TestCase):
    def setUp(self):
        self.func = UniqueEmail()

    def test_1(self):
        emails = [
            "test.email+alex@leetcode.com",
            "test.e.mail+bob.cathy@leetcode.com",
            "testemail+david@lee.tcode.com"
            ]
        expected = 2
        self.assertEqual(self.func.numUniqueEmails(emails), expected)

    def test_2(self):
        emails = [
            "fg.r.u.uzj+o.pw@kziczvh.com",
            "r.cyo.g+d.h+b.ja@tgsg.z.com",
            "fg.r.u.uzj+o.f.d@kziczvh.com",
            "r.cyo.g+ng.r.iq@tgsg.z.com",
            "fg.r.u.uzj+lp.k@kziczvh.com",
            "r.cyo.g+n.h.e+n.g@tgsg.z.com",
            "fg.r.u.uzj+k+p.j@kziczvh.com",
            "fg.r.u.uzj+w.y+b@kziczvh.com",
            "r.cyo.g+x+d.c+f.t@tgsg.z.com",
            "r.cyo.g+x+t.y.l.i@tgsg.z.com",
            "r.cyo.g+brxxi@tgsg.z.com",
            "r.cyo.g+z+dr.k.u@tgsg.z.com",
            "r.cyo.g+d+l.c.n+g@tgsg.z.com",
            "fg.r.u.uzj+vq.o@kziczvh.com",
            "fg.r.u.uzj+uzq@kziczvh.com",
            "fg.r.u.uzj+mvz@kziczvh.com",
            "fg.r.u.uzj+taj@kziczvh.com",
            "fg.r.u.uzj+fek@kziczvh.com"
        ]
        expected = 2
        self.assertEqual(self.func.numUniqueEmails(emails), expected)


if __name__ == '__main__':
    unittest.main()