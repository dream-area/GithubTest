from  werkzeug.security import generate_password_hash,check_password_hash

class User:

    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password_hash = self.save_password(password)

    def check_email(self,email):
        return self.email == email

    def save_password(self,password):
        return generate_password_hash(password)
         

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)



def main():
    userList = []
    print('■■■■■■■■■■■■ welcome ■■■■■■■■■■■■') 
    while 1:
        choose = int(input('''
        请选择：
        1、注册
        2、登录
        3、退出
        '''))

        if choose == 1 :
            print('请输入：')

            name = input('name:')
            email = input('email:')
            password = input('password:')

            newUser = User(name,email,password)
            userList.append(newUser)

            for i in userList:
                print(i.name,i.email,i.password_hash)


        if choose == 2 :
            email_v = 0
            pass_value = 0
            print('请输入：')
            email = input('email:')
            password = input('password:') 
            for userinfo in userList:
                if userinfo.check_email(email):
                    email_v =1
                    if userinfo.check_password(password):
                        pass_value =1
                        #print("Your email & password is correct!")
            if email_v :
                print("Your email is exist!")
                if pass_value:
                    print("You can pass !")
                else:
                    print("Your passoword is not correct!")
            else:
                print("Your email is not exist!")




        if choose == 3 :
            break



if __name__ == '__main__':
    main()

