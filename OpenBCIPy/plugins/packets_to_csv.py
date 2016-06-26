import csv
import timeit
import datetime

import plugin_interface as plugintypes

class PluginPacketsToCSV(plugintypes.IPluginExtended):
    #
    #
    # # __init__
	# def activate(self):
	# 	self.array = []
    #
	# # Called with each new sample
	# def __call__(self, sample):
    #
	# 	if sample:
    #
	# 		#FORMAT OF INCOMING DATA: ID: %f\n%s\n%s" %(sample.id, str(sample.channel_data)[1:-1], str(sample.aux_data)[1:-1])
    #
	# 		key_values_row = []
    #
	# 		# Create an array of : (sample number, s1, s2 ... s8)
    #
	# 		key_values_row.append(sample.id)
    #
	# 		for i in sample.channel_data:
	# 		    key_values_row.append(i)
    #
	# 		# Append row to self.array
	# 		self.array.append(key_values_row)
    #
	# 		if len(self.array) == 512:
	# 		    print self.array
	# 		    print "Yahhaaayyyyy"
    #
	# 		    self.array = []
	foo = 1

	def __init__(self, file_name="collect.csv", delim = ",", verbose=False):
		now = datetime.datetime.now()
		self.time_stamp = '%d-%d-%d_%d-%d-%d'%(now.year,now.month,now.day,now.hour,now.minute,now.second)
		self.file_name = self.time_stamp
		self.start_time = timeit.default_timer()
		self.delim = delim
		self.verbose = verbose


	def activate(self):
        #self.array_packet = 23
        global foo
		foo +=1
		if len(self.args) > 0:
			if 'no_time' in self.args:
				self.file_name = self.args[0]
			else:
				self.file_name = self.args[0] + '_' + self.file_name;
			if 'verbose' in self.args:
				self.verbose = True

		self.file_name = self.file_name + '.csv'
		print "Will export CSV to:", self.file_name
		#Open in append mode
		with open(self.file_name, 'a') as f:
			f.write('%'+self.time_stamp + '\n')

	def deactivate(self):
		print "Closing, CSV saved to:", self.file_name
		return

	def show_help(self):
		print "Optional argument: [filename] (default: collect.csv)"

	def __call__(self, sample):
		t = timeit.default_timer() - self.start_time

		#print timeSinceStart|Sample Id
		if self.verbose:
			print("CSV: %f | %d" %(t,sample.id))

		row = ''
		row += str(t)
		row += self.delim
		row += str(sample.id)
		row += self.delim
		for i in sample.channel_data:
			row += str(i)
			row += self.delim
		for i in sample.aux_data:
			row += str(i)
			row += self.delim
		#remove last comma
		row += '\n'
		with open(self.file_name, 'a') as f:
			f.write(row)
