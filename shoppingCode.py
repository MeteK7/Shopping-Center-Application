import sqlite3

conn=sqlite3.connect('shopDb.db', timeout=10);

chooseDb=conn.cursor();

if(conn):
    print('Baglanti Başarılı!')
else:
    print('Bağlantı Başarısız!')


def registerPage():
    print('--REGISTER PAGE---\n');
    print('Name: ');
    userName=input();
    print('Surname: ');
    userSurname=input();
    print('Password: ')
    userPass=input();
    print('e-mail: ');
    userEmail=input();
    print('Choose one question type and answer: (1-2-3-4)');
    a='Where were you born?';
    b='Where did your parents meet?';
    c='What is your favourite musician?';
    d='What makes you different?';

    print(a+'(1)\n'+b+'(2)\n'+c+'(3)\n'+d+'(4)\n')

    userQues=input();
    if(userQues=='1'):
        userQues=a;
    elif(userQues=='2'):
        userQues=b;
    elif(userQues=='3'):
        userQues=c;
    elif(userQues=='4'):
        userQues=d;

    print('Enter your Answer: ');
    userAnswer=input();

    print('Enter your phone number: ');
    userPhoneNum=input();

    sql ="INSERT INTO userInfo VALUES (?,?,?,?,?,?,?);"

    chooseDb.execute(sql,(userName,userSurname,userPass,userEmail,userQues,userAnswer,userPhoneNum));

    conn.commit();

def loginpage():

    attempt = 0;
    loop='true';

    while loop == 'true':

        print('Please enter your e-mail: ');
        logEmail=input();

        print('Please enter your password: ');
        logPass=input();

        with sqlite3.connect('shopDb.db') as db:
            cursor=db.cursor()

        finduser = ("SELECT * FROM userInfo WHERE userEmail=? AND userPassword=?")
        cursor.execute(finduser, [logEmail, logPass])
        results = cursor.fetchall()

        if results:
            for i in results:
                print("Welcome "+i[0]+"!")
            loop = 'false'
            categories()
            return "exit"

        else:
            print("Username and password not recognised!")
            attempt = attempt+1

            if attempt==3:
                print('Please re-enter your e-mail: ')
                logEmail=input()

                with sqlite3.connect('shopDb.db') as db:
                    cursor = db.cursor()

                finduser = ("SELECT * FROM userInfo WHERE userEmail=?")
                cursor.execute(finduser, [logEmail])
                results = cursor.fetchall()

                if results:
                    for i in results:
                        print('Please write your security answer: \n')
                        print(i[4]+': ')
                        secAnswer = input();
                        if secAnswer==i[5]:
                            print('Change your password:  ')
                            newPass=input();

                            sql = '''UPDATE userInfo SET userPassword=? WHERE userEmail=?'''

                            chooseDb.execute(sql, (newPass, logEmail));

                            conn.commit();
                        else:
                            print('uncorrect answer')

                    return "exit"

                else:
                    print('There is no such e-mail in the Database!\n\n')
                    print('Would you like to sign up? (Y/N)')
                    choice=input();
                    if choice=='Y':
                        loop = 'false'
                        registerPage();
                    else:
                        break


def categories():
    loop='true'

    while loop=='true':

        print('1-COMPUTERS  2-WHITE APPLIANCES  3-SUPERMARKET  4-ELECTRONICS')
        mainCateg = input()

        if 0 < int(mainCateg) < 5:
            subCategories(mainCateg)
            loop = 'false'
        else:
            print ('You entered a false choice!')


def subCategories(mainCateg):
    with sqlite3.connect('shopDb.db') as db:
        cursor = db.cursor()

    if mainCateg=='1':
        print('Laptops or Desktops? (1-2)')
        subCateg=input()
        if subCateg=='1':
            print('---Models for Laptops---\n')
            find = ("SELECT * FROM laptops")

        else:
            print('---Models for Desktops---')
            find = ("SELECT * FROM desktops")
    elif mainCateg=='2':
        print('washing machine or dishwashing machine?(1-2)')
        subCateg=input()
        if subCateg=='1':
            print('Models for washers')
            find = ("SELECT * FROM washers")
        else:
            print('Models for dishwashers')
            find = ("SELECT * FROM dishwashers")
    elif mainCateg=='3':
        print('Teah or Water?(1-2)')
        subCateg=input()
        if subCateg=='1':
            print('Models for tea')
            find = ("SELECT * FROM tea")
        else:
            print('Models for water')
            find = ("SELECT * FROM water")
    elif mainCateg == '4':
        print('Cell Phone or TV?(1-2)')
        subCateg = input()
        if subCateg == '1':
            print('Models for phones')
            find = ("SELECT * FROM cellphone")
        else:
            print('Models for TVs')
            find = ("SELECT * FROM TV")

    cursor.execute(find)
    results = cursor.fetchall()

    if results:
        for i in results:
            print(i)
        return "exit"


print('Please make a choice: ')
print('I would like to do shopping(--1--)')
print('I would just like to surf(--2--)')

x = input();

if(x=='1'):
    print('Please register(1)');
    print('Please login if you have an account(2)');
    x = input();
    if(x=='1'):
        registerPage();
    elif(x=='2'):
        loginpage();

elif(x=='2'):
    categories();

else:
    print('You entered uncorrect key!');

chooseDb.close();
conn.close();