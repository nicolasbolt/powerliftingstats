from flask import Flask, render_template, request
import pandas as pd
from os import path
from build_xml import *
from csv_search_vectorized import *

application = app = Flask(__name__)

@app.route('/')
def lifter_search():
	return render_template('form.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/instructions')
def instructions():
	return render_template('instructions.html')

@app.route('/inquiries')
def inquiries():
	return render_template('inquiries.html')

@app.route('/', methods=['POST'])
def lifter_search_post():
	csv_file = 'openpowerlifting.csv'
	if request.method == 'POST':
		try:
			name = request.form['name']
			fed = request.form['federation']
			wc = request.form['weightclass']
			lifter_search_xml(name, wc, fed)
			dataFrame = create_df('openpowerlifting.csv')
			meet_results = search_csv(name, csv_file, dataFrame)
			max_s = max_squat(meet_results)
			max_b = max_bench(meet_results)
			max_d = max_deadlift(meet_results)
			percents = lifter_percentile(name, wc, fed, meet_results, csv_file, dataFrame)
			squat_percent = percents[0]
			bench_percent = percents[1]
			deadlift_percent = percents[2]
			squat_vs_ee = 100 - squat_percent
			bench_vs_ee = 100 - bench_percent
			deadlift_vs_ee = 100 - deadlift_percent
			return render_template('results.html', name=name, fed=fed, wc=wc, max_s=max_s, max_b=max_b, max_d=max_d, squat_percent=squat_percent, bench_percent=bench_percent, deadlift_percent=deadlift_percent, squat_vs_ee=squat_vs_ee, bench_vs_ee=bench_vs_ee, deadlift_vs_ee=deadlift_vs_ee)
		except:
			return render_template('error_screen.html')
	return render_template('form.html')

@app.route('/compare', methods=['GET', 'POST'])
def compare():
	csv_file = 'openpowerlifting.csv'
	if request.method == 'POST':
		#try:
		name1 = request.form['name1']
		name2 = request.form['name2']
		dataFrame = create_df(csv_file)
		results = lifter_compare(dataFrame, name1, name2)
		squat1 = results[0][0]
		bench1 = results[0][1]
		deadlift1 = results[0][2]
		total1 = results[0][3]
		squat2 = results[1][0]
		bench2 = results[1][1]
		deadlift2 = results[1][2]
		total2 = results[1][3]
		squat_bw1 = results[0][4]
		squat_bw2 = results[1][4]
		bench_bw1 = results[0][5]
		bench_bw2 = results[1][5]
		deadlift_bw1 = results[0][6]
		deadlift_bw2 = results[1][6]
		total_bw1 = results[0][7]
		total_bw2 = results[1][7]

		return render_template('compare_results.html', name1=name1, name2=name2, squat1=squat1, bench1=bench1, deadlift1=deadlift1, squat2=squat2, bench2=bench2, deadlift2=deadlift2, total1=total1, total2=total2, squat_bw1=squat_bw1, squat_bw2=squat_bw2, bench_bw1=bench_bw1, bench_bw2=bench_bw2, deadlift_bw1=deadlift_bw1, deadlift_bw2=deadlift_bw2, total_bw1=total_bw1, total_bw2=total_bw2)
		#except:
		#	return render_template('error_screen.html')
	return render_template('compare.html')

@app.route('/weightclass.html')
def weightclass():
	csv_file = 'openpowerlifting.csv'
	dataFrame = create_df('openpowerlifting.csv')
	data = pull_lifter_data('form_data.xml')
	name = data[0]
	wc = data[1]
	fed = data[2]
	lifts = weightclass_spread(wc, fed, dataFrame)
	s_300 = lifts[0]
	s_400 = lifts[1]
	s_500 = lifts[2]
	s_600 = lifts[3]
	s_700 = lifts[4]
	s_800 = lifts[5]
	s_900 = lifts[6]
	s_1000 = lifts[7]

	b_200 = lifts[8]
	b_300 = lifts[9]
	b_400 = lifts[10]
	b_500 = lifts[11]
	b_600 = lifts[12]
	b_700 = lifts[13]

	d_300 = lifts[14]
	d_400 = lifts[15]
	d_500 = lifts[16]
	d_600 = lifts[17]
	d_700 = lifts[18]
	d_800 = lifts[19]
	d_900 = lifts[20]
	d_1000 = lifts[21]
	return render_template('weightclass.html', name=name, wc=wc, fed=fed, s_300=s_300, s_400=s_400, s_500=s_500, s_600=s_600, s_700=s_700, s_800=s_800, s_900=s_900, s_1000=s_1000,
		b_200=b_200, b_300=b_300, b_400=b_400, b_500=b_500, b_600=b_600, b_700=b_700,
		d_300=d_300, d_400=d_400, d_500=d_500, d_600=d_600, d_700=d_700, d_800=d_800, d_900=d_900, d_1000=d_1000)

@app.route('/greports')
def greports():
	return render_template('general_reports.html')

@app.route('/83_report.html')
def report_83():
	dataFrame = create_df('openpowerlifting.csv')
	lifts = weightclass_spread('83', 'USAPL', dataFrame)
	s_300 = lifts[0]
	s_400 = lifts[1]
	s_500 = lifts[2]
	s_600 = lifts[3]
	s_700 = lifts[4]
	s_800 = lifts[5]
	s_900 = lifts[6]
	s_1000 = lifts[7]

	b_200 = lifts[8]
	b_300 = lifts[9]
	b_400 = lifts[10]
	b_500 = lifts[11]
	b_600 = lifts[12]
	b_700 = lifts[13]

	d_300 = lifts[14]
	d_400 = lifts[15]
	d_500 = lifts[16]
	d_600 = lifts[17]
	d_700 = lifts[18]
	d_800 = lifts[19]
	d_900 = lifts[20]
	d_1000 = lifts[21]
	return render_template('83_report.html', s_300=s_300, s_400=s_400, s_500=s_500, s_600=s_600, s_700=s_700, s_800=s_800, s_900=s_900, s_1000=s_1000,
		b_200=b_200, b_300=b_300, b_400=b_400, b_500=b_500, b_600=b_600, b_700=b_700,
		d_300=d_300, d_400=d_400, d_500=d_500, d_600=d_600, d_700=d_700, d_800=d_800, d_900=d_900, d_1000=d_1000)

@app.route('/105_report.html')
def report_105():
	dataFrame = create_df('openpowerlifting.csv')
	lifts = weightclass_spread('105', 'USAPL', dataFrame)
	s_300 = lifts[0]
	s_400 = lifts[1]
	s_500 = lifts[2]
	s_600 = lifts[3]
	s_700 = lifts[4]
	s_800 = lifts[5]
	s_900 = lifts[6]
	s_1000 = lifts[7]

	b_200 = lifts[8]
	b_300 = lifts[9]
	b_400 = lifts[10]
	b_500 = lifts[11]
	b_600 = lifts[12]
	b_700 = lifts[13]

	d_300 = lifts[14]
	d_400 = lifts[15]
	d_500 = lifts[16]
	d_600 = lifts[17]
	d_700 = lifts[18]
	d_800 = lifts[19]
	d_900 = lifts[20]
	d_1000 = lifts[21]
	return render_template('105_report.html', s_300=s_300, s_400=s_400, s_500=s_500, s_600=s_600, s_700=s_700, s_800=s_800, s_900=s_900, s_1000=s_1000,
		b_200=b_200, b_300=b_300, b_400=b_400, b_500=b_500, b_600=b_600, b_700=b_700,
		d_300=d_300, d_400=d_400, d_500=d_500, d_600=d_600, d_700=d_700, d_800=d_800, d_900=d_900, d_1000=d_1000)

@app.route('/shw_report.html')
def report_shw():
	dataFrame = create_df('openpowerlifting.csv')
	lifts = weightclass_spread('120+', 'USAPL', dataFrame)
	s_300 = lifts[0]
	s_400 = lifts[1]
	s_500 = lifts[2]
	s_600 = lifts[3]
	s_700 = lifts[4]
	s_800 = lifts[5]
	s_900 = lifts[6]
	s_1000 = lifts[7]

	b_200 = lifts[8]
	b_300 = lifts[9]
	b_400 = lifts[10]
	b_500 = lifts[11]
	b_600 = lifts[12]
	b_700 = lifts[13]

	d_300 = lifts[14]
	d_400 = lifts[15]
	d_500 = lifts[16]
	d_600 = lifts[17]
	d_700 = lifts[18]
	d_800 = lifts[19]
	d_900 = lifts[20]
	d_1000 = lifts[21]
	return render_template('shw_report.html', s_300=s_300, s_400=s_400, s_500=s_500, s_600=s_600, s_700=s_700, s_800=s_800, s_900=s_900, s_1000=s_1000,
		b_200=b_200, b_300=b_300, b_400=b_400, b_500=b_500, b_600=b_600, b_700=b_700,
		d_300=d_300, d_400=d_400, d_500=d_500, d_600=d_600, d_700=d_700, d_800=d_800, d_900=d_900, d_1000=d_1000)

@app.route('/usapl_report.html')
def report_usapl():
	dataFrame = create_df('openpowerlifting.csv')
	lifts = fed_spread(dataFrame, 'USAPL')
	s_300 = lifts[0]
	s_400 = lifts[1]
	s_500 = lifts[2]
	s_600 = lifts[3]
	s_700 = lifts[4]
	s_800 = lifts[5]
	s_900 = lifts[6]
	s_1000 = lifts[7]

	b_200 = lifts[8]
	b_300 = lifts[9]
	b_400 = lifts[10]
	b_500 = lifts[11]
	b_600 = lifts[12]
	b_700 = lifts[13]

	d_300 = lifts[14]
	d_400 = lifts[15]
	d_500 = lifts[16]
	d_600 = lifts[17]
	d_700 = lifts[18]
	d_800 = lifts[19]
	d_900 = lifts[20]
	d_1000 = lifts[21]
	return render_template('usapl_report.html', s_300=s_300, s_400=s_400, s_500=s_500, s_600=s_600, s_700=s_700, s_800=s_800, s_900=s_900, s_1000=s_1000,
		b_200=b_200, b_300=b_300, b_400=b_400, b_500=b_500, b_600=b_600, b_700=b_700,
		d_300=d_300, d_400=d_400, d_500=d_500, d_600=d_600, d_700=d_700, d_800=d_800, d_900=d_900, d_1000=d_1000)

@app.route('/uspa_report.html')
def report_uspa():
	dataFrame = create_df('openpowerlifting.csv')
	lifts = fed_spread(dataFrame, 'USPA')
	s_300 = lifts[0]
	s_400 = lifts[1]
	s_500 = lifts[2]
	s_600 = lifts[3]
	s_700 = lifts[4]
	s_800 = lifts[5]
	s_900 = lifts[6]
	s_1000 = lifts[7]

	b_200 = lifts[8]
	b_300 = lifts[9]
	b_400 = lifts[10]
	b_500 = lifts[11]
	b_600 = lifts[12]
	b_700 = lifts[13]

	d_300 = lifts[14]
	d_400 = lifts[15]
	d_500 = lifts[16]
	d_600 = lifts[17]
	d_700 = lifts[18]
	d_800 = lifts[19]
	d_900 = lifts[20]
	d_1000 = lifts[21]
	return render_template('uspa_report.html', s_300=s_300, s_400=s_400, s_500=s_500, s_600=s_600, s_700=s_700, s_800=s_800, s_900=s_900, s_1000=s_1000,
		b_200=b_200, b_300=b_300, b_400=b_400, b_500=b_500, b_600=b_600, b_700=b_700,
		d_300=d_300, d_400=d_400, d_500=d_500, d_600=d_600, d_700=d_700, d_800=d_800, d_900=d_900, d_1000=d_1000)