from flask import Flask,render_template, request, redirect
from flask_mysqldb import MySQL
form=""
to=""
way=""
vehicle=""
data=[]
app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'tollbooth'

mysql = MySQL(app)



@app.route("/index.html", methods=['GET', 'POST'])
def index():
    global form,to,way,vehicle
    if request.method == 'POST':
        form = request.form.get("from")
        to = request.form.get("to")
        way = request.form.get("way")
        vehicle = request.form.get("vehicle")

        
    print(form)
    print(to)
    print(way)
    print(vehicle)


    return render_template("index.html")

@app.route("/about.html")
def index1():
    return render_template("about.html")

@app.route("/login.html", methods=['GET', 'POST'])
def index2():
    if request.method == 'POST':
        # Fetch form data
        username = request.form.get("Username")
        password = request.form.get("Password")

        cur = mysql.connection.cursor()
        sql="SELECT register_username from register where register_username=%s"
        try:
            cur.execute(sql,[username])
            usernamedata = cur.fetchone()
            unm=usernamedata[0]
        except:
            return redirect('/login.html')
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT register_password from register where register_username=%s", [username])
        passworddata = cur.fetchone()[0]


        if passworddata==password and username==unm:
            return redirect('/index.html')
        else:
            return redirect('/login.html')

    return render_template("login.html")

@app.route("/register.html", methods=['GET', 'POST'])
def index3():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        firstname = userDetails['firstname']
        lastname = userDetails['lastname']
        email = userDetails['Email']
        mobile = userDetails['Mobile']
        username = userDetails['Username']
        password = userDetails['Password']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO register(register_first, register_last, register_email, register_mobile, register_username, register_password) VALUES(%s, %s, %s, %s, %s, %s)",(firstname, lastname, email, mobile, username, password))
        mysql.connection.commit()
        cur.close()
        return redirect('/login.html')
    return render_template("register.html")
   


@app.route("/404.html")
def index4():
    return render_template("404.html")


@app.route("/contact.html")
def index5():
    return render_template("contact.html")

@app.route("/gallery.html", methods=['GET', 'POST'])
def index6():
    global form,to,way,vehicle,data
    if request.method == 'POST':
        form = request.form.get("from")
        to = request.form.get("to")
        way = request.form.get("way")
        if str(way)=="1 WAY":
        	way=1
        else:
        	way=2	
        vehicle = request.form.get("vehicle")
        if str(vehicle)=="CAR / JEEP  ":
        	vehicle=1
        elif str(vehicle)=="LORRY / TRUCK":
        	vehicle=3
        else:
        	vehicle=2
        print("hi")

        #cur = mysql.connection.cursur()

        #sql="SELECT "
    print(form)
    print(to)
    print(way)
    print(vehicle)
    cur = mysql.connection.cursor()
    cur.execute("SELECT * from tolls where tolls_from=%s and tolls_to=%s", [form,to])
      #sworddata = cur.fetchone()[0]
    #que="SELECT * from tolls where tolls_from=";
    #cur.execute(que)
    data=[]
    for i in cur:
        data=data+[i]   
    for i in range(len(data)):
    	data[i]=list(data[i])
    	data[i][3]=int(data[i][3])*way*vehicle  	
    for i in range(len(data)):
    	data[i]=tuple(data[i])
    print(data)	


    return render_template("gallery.html",data=data)



@app.route("/card.html", methods = ['GET' , 'POST'])
def index8():
    if request.method == 'POST':
        # Fetch form data
        name = request.form.get("name")
        cardnum = request.form.get("number")
        month = request.form.get("month")
        year = request.form.get("year")
        cvv = request.form.get("cvv")
        print(name)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO card(name, cardnum, month, year, cvv) VALUES (%s, %s, %s, %s, %s)",(name, cardnum, month, year, cvv))
        mysql.connection.commit()
        cur.close()
        return redirect('/QR1.html')
    return render_template("card.html")  

@app.route("/QR1.html",methods =['GET','POST'])
def index9():
    
    return render_template('QR1.html')

@app.route("/package.html",methods =['GET','POST'])
def index10():
    global data
    checked=[]
    count=0
    for i in data:
    	if str(request.form.get(i[0]))=='checked':
    		checked.append(count)
    	count+=1
    result=[]
    total=0
    for i in checked:
    	result.append(data[i])
    	total+=int(data[i][3])
    print(result)	

    		
    return render_template('package.html',data=[result,total])



if __name__== '__main__':
	app.debug = True
	app.run(host='0.0.0.0',port=5000)


