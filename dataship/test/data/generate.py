#! /usr/bin/env python3
import os
import numpy as np

DATA_DIR = "0001/";

doric = np.zeros(100, dtype=np.float32)
tuscan = np.zeros(100, dtype=np.uint8)
composite = np.zeros(100, dtype=np.int32)


doric[0] = 3.141592;
doric[23] = 1.010101010;
doric[78] = 2.7182818;

tuscan[0] = 7;
tuscan[13] = 37;
tuscan[34] = 89;

composite[0] = 8956
composite[37] = 13
composite[78] = 78

os.makedirs(DATA_DIR, exist_ok=True)

with open(DATA_DIR+"doric.f32", "wb") as f:
	f.write(doric.tostring())

with open(DATA_DIR+"tuscan.u8", "wb") as f:
	f.write(tuscan.tostring())

with open(DATA_DIR+"composite.i32", "wb") as f:
	f.write(composite.tostring())
