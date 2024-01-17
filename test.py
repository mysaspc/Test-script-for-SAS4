import sys, os, time, re
sys.path.append(r'C:\Users\Public\Documents\LeCroy\SAS4 Protocol Suite\API\SDK\Bin')
import TLSASAPI


def opentrace(trace_file):
	open_trace = TLSASAPI.OpenFile(trace_file)
	total_packet_in_trace = open_trace.GetCount()
	if total_packet_in_trace != 0:
		return("Passed")
	else:
		return("Failed")
	
print(opentrace("C:\\Users\\Public\\Documents\\LeCroy\\SAS4 Protocol Suite\\Examples\\Traces\\AfterJammer Modified SCSICommand.sxt"))
# last updated by OS machine at 3:44pm

# received the update by workstation at 5:21pm

# new change by mysaspc at 5:36pm

print("From OS machine user - please make sure this is seen and executed by Jenkins: 17-Jan 10:12am")

