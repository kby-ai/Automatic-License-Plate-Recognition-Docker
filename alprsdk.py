import os

from ctypes import *

libPath = os.path.abspath(os.path.dirname(__file__)) + '/libalpr.so'
alprsdk = cdll.LoadLibrary(libPath)

getMachineCode = alprsdk.getMachineCode
getMachineCode.argtypes = []
getMachineCode.restype = c_char_p

setActivation = alprsdk.setActivation
setActivation.argtypes = [c_char_p]
setActivation.restype = c_int32

initSDK = alprsdk.initSDK
initSDK.argtypes = []
initSDK.restype = c_int32

getLicensePlate = alprsdk.get_license_using_bytes
getLicensePlate.argtypes = [c_char_p, c_ulong, POINTER(POINTER(c_char_p)), POINTER(c_int), POINTER(c_float)]
getLicensePlate.restype = c_int32

freeLicenseResults = alprsdk.free_license_results
freeLicenseResults.argtypes = [POINTER(c_char_p), c_int]
freeLicenseResults.restype = None
