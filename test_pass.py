import unittest
import passwordManager
import hibp

class TestPass(unittest.TestCase):
    def test_checkingSpecialChar(self):
        self.assertTrue(passwordManager.checkingPass("Haider1234%$"))


    def test_checkingmasterpas(self):
        p= "test"
        self.assertTrue(passwordManager.masterHashComapare(p))

    def test_checkingpassLength(self):
        self.assertTrue(passwordManager.checkingPass("a2!@"))


    def test_checkinghaveibeenpawned(self):
        self.assertTrue(hibp.checkingPasswords("test123")) 


    def test_checkusers(self):
        self.assertTrue(passwordManager.readCsv("hsoffenburg"))

    def test_checknuminpass(self):
        self.assertTrue(passwordManager.checkingPass("Number123%^")) 


    def test_checkuupercaseinpass(self):
        self.assertTrue(passwordManager.checkingPass("Test123$%")) 



if __name__ == '__main__':
    unittest.main()