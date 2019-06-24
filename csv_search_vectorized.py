from os import path
import pandas as pd

def create_df(file):
	current_dir = path.dirname(__file__)
	csv_columns = ['Name', 'Sex', 'Event', 'Equipment', 'BodyweightKg', 'WeightClassKg', 'Best3SquatKg', 'Best3BenchKg', 'Best3DeadliftKg', 'TotalKg', 'Federation']
	dataFrame = pd.read_csv(path.join(current_dir, file), usecols=csv_columns)
	dataFrame.fillna(0, inplace=True)
	return dataFrame


def search_csv(name, file, dataFrame):
	squat_nums = []
	bench_nums = []
	deadlift_nums = []
	lifter_list = []
	filter = dataFrame["Name"] == name
	name_df = dataFrame[dataFrame['Name'] == name]
	for squats in name_df.loc[:,'Best3SquatKg']:
		squat_nums.append(squats)
	for benches in name_df.loc[:,'Best3BenchKg']:
		bench_nums.append(benches)
	for deadlifts in name_df.loc[:,'Best3DeadliftKg']:
		deadlift_nums.append(deadlifts)

	lifter_list.append(squat_nums)
	lifter_list.append(bench_nums)
	lifter_list.append(deadlift_nums)

	return lifter_list

def max_squat(lifter_list):
	return max(lifter_list[0])

def max_bench(lifter_list):	
	return max(lifter_list[1])

def max_deadlift(lifter_list):	
	return max(lifter_list[2])

	
def lifter_percentile(name, wc, fed, lifter_list, file, dataFrame):
	ms = max_squat(lifter_list)
	mb = max_bench(lifter_list)
	md = max_deadlift(lifter_list)
	data = dataFrame[['WeightClassKg', 'Federation', 'Event', 'Equipment', 'Best3SquatKg', 'Best3BenchKg', 'Best3DeadliftKg']].copy()
	df = data[(data['WeightClassKg'] == wc) & (data['Federation'] == fed) & (data['Event'] == 'SBD') & (data['Equipment'] == 'Raw')]
	s_above = len(df[df['Best3SquatKg'] > ms])
	b_above = len(df[df['Best3BenchKg'] > mb])
	d_above = len(df[df['Best3DeadliftKg'] > md])
	total = len(df)
	final_list = [b_above, total]
	squat_percent = round(s_above / total * 100,2)
	bench_percent = round(b_above / total * 100,2)
	deadlift_percent = round(d_above / total * 100,2)

	percent_list = [squat_percent, bench_percent, deadlift_percent]

	return percent_list

def weightclass_spread( wc, fed, dataFrame):
	data = dataFrame[['WeightClassKg', 'Federation', 'Event', 'Equipment', 'Best3SquatKg', 'Best3BenchKg', 'Best3DeadliftKg']].copy()
	df = data[(data['WeightClassKg'] == wc) & (data['Federation'] == fed) & (data['Event'] == 'SBD') & (data['Equipment'] == 'Raw')]
	
	s_300 = 0
	s_400 = 0
	s_500 = 0
	s_600 = 0
	s_700 = 0
	s_800 = 0
	s_900 = 0
	s_1000 = 0

	b_200 = 0
	b_300 = 0
	b_400 = 0
	b_500 = 0
	b_600 = 0
	b_700 = 0

	d_300 = 0
	d_400 = 0
	d_500 = 0
	d_600 = 0
	d_700 = 0
	d_800 = 0
	d_900 = 0
	d_1000 = 0

	for i in df.iterrows():
		if dataFrame.loc[i[0],'Best3SquatKg'] > 136.0 and dataFrame.loc[i[0],'Best3SquatKg'] < 181.0:
			s_300 += 1
		elif dataFrame.loc[i[0],'Best3SquatKg'] > 181.0 and dataFrame.loc[i[0],'Best3SquatKg'] < 226.5:
			s_400 += 1
		elif dataFrame.loc[i[0],'Best3SquatKg'] > 226.5 and dataFrame.loc[i[0],'Best3SquatKg'] < 272.0:
			s_500 += 1
		elif dataFrame.loc[i[0],'Best3SquatKg'] > 272.0 and dataFrame.loc[i[0],'Best3SquatKg'] < 317.0:
			s_600 += 1
		elif dataFrame.loc[i[0],'Best3SquatKg'] > 317.5 and dataFrame.loc[i[0],'Best3SquatKg'] < 363.0:
			s_700 += 1
		elif dataFrame.loc[i[0],'Best3SquatKg'] > 363.0 and dataFrame.loc[i[0],'Best3SquatKg'] < 408.0:
			s_800 += 1
		elif dataFrame.loc[i[0],'Best3SquatKg'] > 408.0 and dataFrame.loc[i[0],'Best3SquatKg'] < 453.5:
			s_900 += 1
		elif dataFrame.loc[i[0],'Best3SquatKg'] > 453.5:	
			s_1000 += 1

		if dataFrame.loc[i[0],'Best3BenchKg'] > 136.0 and dataFrame.loc[i[0],'Best3BenchKg'] < 181.0:
			b_300 += 1
		elif dataFrame.loc[i[0],'Best3BenchKg'] > 181.0 and dataFrame.loc[i[0],'Best3BenchKg'] < 226.5:
			b_400 += 1
		elif dataFrame.loc[i[0],'Best3BenchKg'] > 226.5 and dataFrame.loc[i[0],'Best3BenchKg'] < 272.0:
			b_500 += 1
		elif dataFrame.loc[i[0],'Best3BenchKg'] > 272.0 and dataFrame.loc[i[0],'Best3BenchKg'] < 317.5:
			b_600 += 1
		elif dataFrame.loc[i[0],'Best3BenchKg'] > 317.5:
			b_700 += 1

		if dataFrame.loc[i[0],'Best3DeadliftKg'] > 136.0 and dataFrame.loc[i[0],'Best3DeadliftKg'] < 181.0:
			d_300 += 1
		elif dataFrame.loc[i[0],'Best3DeadliftKg'] > 181.0 and dataFrame.loc[i[0],'Best3DeadliftKg'] < 226.5:
			d_400 += 1
		elif dataFrame.loc[i[0],'Best3DeadliftKg'] > 226.5 and dataFrame.loc[i[0],'Best3DeadliftKg'] < 272.0:
			d_500 += 1
		elif dataFrame.loc[i[0],'Best3DeadliftKg'] > 272.0 and dataFrame.loc[i[0],'Best3DeadliftKg'] < 317.5:
			d_600 += 1
		elif dataFrame.loc[i[0],'Best3DeadliftKg'] > 317.5 and dataFrame.loc[i[0],'Best3DeadliftKg'] < 363.0:
			d_700 += 1
		elif dataFrame.loc[i[0],'Best3DeadliftKg'] > 363.0 and dataFrame.loc[i[0],'Best3DeadliftKg'] < 408.0:
			d_800 += 1
		elif dataFrame.loc[i[0],'Best3DeadliftKg'] > 408.0 and dataFrame.loc[i[0],'Best3DeadliftKg'] < 453.5:
			d_900 += 1
		elif dataFrame.loc[i[0],'Best3DeadliftKg'] > 453.5:	
			d_1000 += 1

	weight_class_list = [
	s_300, #0
	s_400, #1
	s_500, #2
	s_600, #3
	s_700, #4
	s_800, #5
	s_900, #6
	s_1000, #7
	b_200, #8
	b_300, #9
	b_400, #10
	b_500, #11
	b_600, #12
	b_700, #13
	d_300, #14
	d_400, #15
	d_500, #16
	d_600, #17
	d_700, #18
	d_800, #19
	d_900, #20
	d_1000, #21
	]

	return weight_class_list

def fed_spread(dataFrame, fed):
	s_300 = 0
	s_400 = 0
	s_500 = 0
	s_600 = 0
	s_700 = 0
	s_800 = 0
	s_900 = 0
	s_1000 = 0

	b_200 = 0
	b_300 = 0
	b_400 = 0
	b_500 = 0
	b_600 = 0
	b_700 = 0

	d_300 = 0
	d_400 = 0
	d_500 = 0
	d_600 = 0
	d_700 = 0
	d_800 = 0
	d_900 = 0
	d_1000 = 0

	data = dataFrame[['WeightClassKg', 'Federation', 'Event', 'Equipment', 'Best3SquatKg', 'Best3BenchKg', 'Best3DeadliftKg']].copy()
	df = data[(data['Federation'] == fed) & (data['Event'] == 'SBD') & (data['Equipment'] == 'Raw')]

	for i in df.iterrows():
		if df.loc[i[0],'Best3SquatKg'] > 136.0 and df.loc[i[0],'Best3SquatKg'] < 181.0:
			s_300 += 1
		elif df.loc[i[0],'Best3SquatKg'] > 181.0 and df.loc[i[0],'Best3SquatKg'] < 226.5:
			s_400 += 1
		elif df.loc[i[0],'Best3SquatKg'] > 226.5 and df.loc[i[0],'Best3SquatKg'] < 272.0:
			s_500 += 1
		elif df.loc[i[0],'Best3SquatKg'] > 272.0 and df.loc[i[0],'Best3SquatKg'] < 317.0:
			s_600 += 1
		elif df.loc[i[0],'Best3SquatKg'] > 317.5 and df.loc[i[0],'Best3SquatKg'] < 363.0:
			s_700 += 1
		elif df.loc[i[0],'Best3SquatKg'] > 363.0 and df.loc[i[0],'Best3SquatKg'] < 408.0:
			s_800 += 1
		elif df.loc[i[0],'Best3SquatKg'] > 408.0 and df.loc[i[0],'Best3SquatKg'] < 453.5:
			s_900 += 1
		elif df.loc[i[0],'Best3SquatKg'] > 453.5:	
			s_1000 += 1

		if df.loc[i[0],'Best3BenchKg'] > 136.0 and df.loc[i[0],'Best3BenchKg'] < 181.0:
			b_300 += 1
		elif df.loc[i[0],'Best3BenchKg'] > 181.0 and df.loc[i[0],'Best3BenchKg'] < 226.5:
			b_400 += 1
		elif df.loc[i[0],'Best3BenchKg'] > 226.5 and df.loc[i[0],'Best3BenchKg'] < 272.0:
			b_500 += 1
		elif df.loc[i[0],'Best3BenchKg'] > 272.0 and df.loc[i[0],'Best3BenchKg'] < 317.5:
			b_600 += 1
		elif df.loc[i[0],'Best3BenchKg'] > 317.5:
			b_700 += 1

		if df.loc[i[0],'Best3DeadliftKg'] > 136.0 and df.loc[i[0],'Best3DeadliftKg'] < 181.0:
			d_300 += 1
		elif df.loc[i[0],'Best3DeadliftKg'] > 181.0 and df.loc[i[0],'Best3DeadliftKg'] < 226.5:
			d_400 += 1
		elif df.loc[i[0],'Best3DeadliftKg'] > 226.5 and df.loc[i[0],'Best3DeadliftKg'] < 272.0:
			d_500 += 1
		elif df.loc[i[0],'Best3DeadliftKg'] > 272.0 and df.loc[i[0],'Best3DeadliftKg'] < 317.5:
			d_600 += 1
		elif df.loc[i[0],'Best3DeadliftKg'] > 317.5 and df.loc[i[0],'Best3DeadliftKg'] < 363.0:
			d_700 += 1
		elif df.loc[i[0],'Best3DeadliftKg'] > 363.0 and df.loc[i[0],'Best3DeadliftKg'] < 408.0:
			d_800 += 1
		elif df.loc[i[0],'Best3DeadliftKg'] > 408.0 and df.loc[i[0],'Best3DeadliftKg'] < 453.5:
			d_900 += 1
		elif df.loc[i[0],'Best3DeadliftKg'] > 453.5:	
			d_1000 += 1

	weight_class_list = [
	s_300, #0
	s_400, #1
	s_500, #2
	s_600, #3
	s_700, #4
	s_800, #5
	s_900, #6
	s_1000, #7
	b_200, #8
	b_300, #9
	b_400, #10
	b_500, #11
	b_600, #12
	b_700, #13
	d_300, #14
	d_400, #15
	d_500, #16
	d_600, #17
	d_700, #18
	d_800, #19
	d_900, #20
	d_1000, #21
	]

	return weight_class_list


def lifter_compare(dataFrame, name1, name2):
	pass
	#Compare best lifts to bodyweight
	#Create Javascript chart to display lift to bodyweight and to compare best lifts

	squat_nums1 = []
	bench_nums1 = []
	deadlift_nums1 = []
	squat_nums2 = []
	bench_nums2 = []
	deadlift_nums2 = []
	total_nums1 = []
	total_nums2 = []

	total1 = 0 
	total2 = 0

	lifters_list = []
	#filter = dataFrame["Name"] == name1
	name_df1 = dataFrame[dataFrame['Name'] == name1]
	name_df2 = dataFrame[dataFrame['Name'] == name2]
	for squats in name_df1.loc[:,'Best3SquatKg']:
		squat_nums1.append(squats)
	for benches in name_df1.loc[:,'Best3BenchKg']:
		bench_nums1.append(benches)
	for deadlifts in name_df1.loc[:,'Best3DeadliftKg']:
		deadlift_nums1.append(deadlifts)
	for totals in name_df1.loc[:,'TotalKg']:
		total_nums1.append(totals)

	for squats in name_df2.loc[:,'Best3SquatKg']:
		squat_nums2.append(squats)
	for benches in name_df2.loc[:,'Best3BenchKg']:
		bench_nums2.append(benches)
	for deadlifts in name_df2.loc[:,'Best3DeadliftKg']:
		deadlift_nums2.append(deadlifts)
	for totals in name_df1.loc[:,'TotalKg']:
		total_nums2.append(totals)

	msquat_nums1 = max(squat_nums1)
	mbench_nums1 = max(bench_nums1)
	mdeadlift_nums1 = max(deadlift_nums1)
	mtotal_nums1 = max(total_nums1)

	msquat_nums2 = max(squat_nums2)
	mbench_nums2 = max(bench_nums2)
	mdeadlift_nums2 = max(deadlift_nums2)
	mtotal_nums2 = max(total_nums2)

	best_meet1 = name_df1[name_df1['TotalKg'] == mtotal_nums1]
	best_meet2 = name_df2[name_df2['TotalKg'] == mtotal_nums2]

	wc1 = best_meet1.iloc[0, 4]
	wc2 = best_meet2.iloc[0, 4]

	squat_bw1 = round(msquat_nums1 / wc1, 2)
	squat_bw2 = round(msquat_nums2 / wc2, 2)

	bench_bw1 = round(mbench_nums1 / wc1, 2)
	bench_bw2 = round(mbench_nums2 / wc2, 2)

	deadlift_bw1 = round(mdeadlift_nums1 / wc1, 2)
	deadlift_bw2 = round(mdeadlift_nums2 / wc2, 2)

	total_bw1 = round(mtotal_nums1 / wc1, 2)
	total_bw2 = round(mtotal_nums2 / wc2, 2)

	lifters_list = [[msquat_nums1, mbench_nums1, mdeadlift_nums1, mtotal_nums1, squat_bw1, bench_bw1, deadlift_bw1, total_bw1], [msquat_nums2, mbench_nums2, mdeadlift_nums2, mtotal_nums2, squat_bw2, bench_bw2, deadlift_bw2, total_bw2]]

	return lifters_list