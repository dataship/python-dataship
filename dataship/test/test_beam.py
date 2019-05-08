
import sys
import unittest
import numpy as np
import os
import shutil

sys.path.append('../../')
from dataship import beam

BASE_DIR = "./data/"
DATA_DIR = BASE_DIR + "0001/";

INDEX = {
	"doric" : "doric.f32",
	"tuscan" : "tuscan.u8",
	"composite" : "composite.i32"
};

# close comparison constants
RTOL = 1e-05
ATOL = 1e-07


class TestBeam(unittest.TestCase):

	def test_number_of_columns_and_keys(self):

		# TODO add test for key columns
		(columns, _) = beam.load(DATA_DIR, INDEX)

		expected = 3
		actual = len(columns.keys())
		self.assertEqual(actual, expected)

	def test_column_names(self):

		(columns, _) = beam.load(DATA_DIR, INDEX)
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

		(columns, _) = beam.load(DATA_DIR, INDEX)
		doric = columns["doric"]
		self.assertEqual(type(doric), np.ndarray)
		self.assertEqual(doric.dtype, np.float32)

	def test_values_float32(self):

		(columns, _) = beam.load(DATA_DIR, INDEX)
		doric = columns["doric"]
		self.assertTrue(np.isclose(doric[0], 3.14159, RTOL, ATOL))
		self.assertTrue(np.isclose(doric[23], 1.0101010, RTOL, ATOL))
		self.assertTrue(np.isclose(doric[78], 2.7182818, RTOL, ATOL))

	def test_type_uint8(self):

		(columns, _) = beam.load(DATA_DIR, INDEX)
		tuscan = columns["tuscan"]
		self.assertEqual(type(tuscan), np.ndarray)
		self.assertEqual(tuscan.dtype, np.uint8)

	def test_values_uint8(self):

		(columns, _) = beam.load(DATA_DIR, INDEX)
		tuscan = columns["tuscan"]
		self.assertTrue(np.isclose(tuscan[0], 7, RTOL, ATOL))
		self.assertTrue(np.isclose(tuscan[13], 37, RTOL, ATOL))
		self.assertTrue(np.isclose(tuscan[34], 89, RTOL, ATOL))

	def test_type_int32(self):

		(columns, _) = beam.load(DATA_DIR, INDEX)
		composite = columns["composite"]
		self.assertEqual(type(composite), np.ndarray)
		self.assertEqual(composite.dtype, np.int32)

	def test_values_int32(self):

		(columns, _) = beam.load(DATA_DIR, INDEX)
		composite = columns["composite"]
		self.assertTrue(np.isclose(composite[0], 8956, RTOL, ATOL))
		self.assertTrue(np.isclose(composite[37], 13, RTOL, ATOL))
		self.assertTrue(np.isclose(composite[78], 78, RTOL, ATOL))

	def test_write_and_read(self):

		test_columns = {
			"test_a" : np.zeros(100, dtype="uint8"),
			"test_b" : np.zeros(100, dtype="float32"),
			"test_c" : np.zeros(100, dtype="int32"),
			"test_d" : list(range(0, 100)),
			"test_e" : [""] * 100
		}

		test_columns["test_a"][11] = 53
		test_columns["test_b"][67] = 3.1415
		test_columns["test_c"][2] = 66532
		test_columns["test_e"][45] = "hello"

		write_dir = BASE_DIR  + "9999/"
		if os.path.exists(write_dir):
			shutil.rmtree(write_dir)

		os.makedirs(write_dir)


		beam.write(write_dir, test_columns)

		(columns, keys) = beam.read(write_dir)

		for column_name in test_columns.keys():

			self.assertTrue(column_name in columns)
			if(type(test_columns[column_name]) == np.ndarray):
				self.assertTrue(np.allclose(test_columns[column_name], columns[column_name]))
			elif(type(test_columns[column_name]) == list):
				self.assertTrue(test_columns[column_name] == columns[column_name])

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
