from flask import Flask,render_template,request,url_for


app=Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/cv')
def cv():
    return render_template("cv.html")
@app.route('/edit_cv')
def edit_cv():
    return render_template("edit_cv.html")

@app.route('/send_personal_info',methods=['GET','POST'])
def send_personal_info():
    if (request.method=='POST'):
        getFirstName=request.form['first_name']
        getLastName=request.form['last_name']
        getAddress1=request.form['address_line1']
        getAddress2=request.form['address_line2']
        getPhone=request.form['phone']
        getEmail=request.form['email']
        getDob=request.form['dob']
        getProfession=request.form['profession']
        getSummary=request.form['summary']
        
        getExpPosition1=request.form['exp_position1']
        getExpCompany1=request.form['exp_company1']
        getDateFrom=request.form['exp_year_from']
        getDateTo=request.form['exp_year_to']
        
        
        
        

        getSchool=request.form['school']
        getSchoolDateFrom=request.form['school_date_from']
        getSchoolDateTo=request.form['school_date_to']
        getSchoolPercentage=request.form['school_percentage']
        getCollege=request.form['college']
        getCollegeDateFrom=request.form['college_date_from']
        getCollegeDateTo=request.form['college_date_to']
        getCollegePercentage=request.form['college_percentage']




        
        return render_template("result.html",passCollegePercentage=getCollegePercentage,passSchoolPercentage=getSchoolPercentage,passFirstName=getFirstName,passLastName=getLastName,passEmail=getEmail,passAddress1=getAddress1,passAddress2=getAddress2,passDob=getDob,passPhone=getPhone,passSummary=getSummary,passExpPosition1=getExpPosition1,passExpCompany1=getExpCompany1,passDateFrom=getDateFrom,passDateTo=getDateTo,passSchool=getSchool,passSchoolDateFrom=getSchoolDateFrom,passSchoolDateTo=getSchoolDateTo,passCollege=getCollege,passCollegeDateFrom=getCollegeDateFrom,passCollegeDateTo=getCollegeDateTo,passProfession=getProfession)  
# @app.route('/send_summary',methods=['GET','POST'])
# def send_summary():

#         getSummary=request.form['summary']
#         return render_template("resul")

if (__name__ == '__main__'):
   app.run(debug=True)