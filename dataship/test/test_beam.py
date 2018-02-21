
import sys
import unittest
import numpy as np

sys.path.append('../../')
from dataship import beam

DATA_DIR = "./data/0001/";

INDEX = {
	"doric" : "doric.f32",
	"tuscan" : "tuscan.u8",
	"composite" : "composite.i32"
};

# close comparison constants
RTOL = 1e-05,
ATOL = 1e-07;

class TestBeam(unittest.TestCase):

	def test_number_of_columns_and_keys(self):

		# TODO add test for key columns
		columns = beam.load(DATA_DIR, INDEX)

		expected = 3
		actual = len(columns.keys())
		self.assertEqual(actual, expected)

	def test_column_names(self):

		columns = beam.load(DATA_DIR, INDEX)
		self.assertTrue("doric" in columns)
		self.assertTrue("tuscan" in columns)
		self.assertTrue("composite" in columns)
		#self.assertTrue("ionic" in columns)
		#self.assertTrue("corinthian" in columns)


# tape("correctly named keys", function(t){
# 	t.plan(2);
#
# 	beam.load(dir, index, function(err, results){
#
# 		t.assert("ionic" in results.keys, "key present");
# 		t.assert("corinthian" in results.keys, "key present");
# 	});
# });
#

	def test_type_float32(self):

		columns = beam.load(DATA_DIR, INDEX)
		doric = columns["doric"]
		self.assertEqual(type(doric), np.ndarray)
		self.assertEqual(doric.dtype, np.float32)

	def test_values_float32(self):

		columns = beam.load(DATA_DIR, INDEX)
		doric = columns["doric"]
		self.assertTrue(np.isclose(doric[0], 3.14159, RTOL, ATOL))
		self.assertTrue(np.isclose(doric[23], 1.0101010, RTOL, ATOL))
		self.assertTrue(np.isclose(doric[78], 2.7182818, RTOL, ATOL))

	def test_type_uint8(self):
		columns = beam.load(DATA_DIR, INDEX)
		tuscan = columns["tuscan"]
		self.assertEqual(type(tuscan), np.ndarray)
		self.assertEqual(tuscan.dtype, np.uint8)

	def test_values_uint8(self):
		columns = beam.load(DATA_DIR, INDEX)
		tuscan = columns["tuscan"]
		self.assertTrue(np.isclose(tuscan[0], 7, RTOL, ATOL))
		self.assertTrue(np.isclose(tuscan[13], 37, RTOL, ATOL))
		self.assertTrue(np.isclose(tuscan[34], 89, RTOL, ATOL))

	def test_type_int32(self):
		columns = beam.load(DATA_DIR, INDEX)
		composite = columns["composite"]
		self.assertEqual(type(composite), np.ndarray)
		self.assertEqual(composite.dtype, np.int32)

	def test_values_int32(self):
		columns = beam.load(DATA_DIR, INDEX)
		composite = columns["composite"]
		self.assertTrue(np.isclose(composite[0], 8956, RTOL, ATOL))
		self.assertTrue(np.isclose(composite[37], 13, RTOL, ATOL))
		self.assertTrue(np.isclose(composite[78], 78, RTOL, ATOL))

#
# tape("keys have correct values", function(t){
# 	t.plan(4);
#
# 	beam.load(dir, index, function(err, results){
#
# 		var ionic_k = results.keys["ionic"];
# 		t.equal(ionic_k[0], "volute", "key values correct");
# 		t.equal(ionic_k[1], "abacus", "key values correct");
# 		t.equal(ionic_k[2], "shaft", "key values correct");
# 		t.equal(ionic_k[3], "base", "key values correct");
# 	});
# });

def main():
	unittest.main()

if __name__ == '__main__':
	main()
