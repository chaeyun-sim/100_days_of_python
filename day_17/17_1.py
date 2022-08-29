class User:
    # pass
    # def __init__(self):
        # print("New user being created ... ")
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follower(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)
print(user_1.followers) #0
print(user_1.following) #1
print(user_2.followers) #1
print(user_2.following) #0



# user_1.id = "001"
# user_1.username = "angela"
print(user_1.username) # angela

# 객체가 초기화 될때 변수나 카운터의 시작 값을 지정할 수 있음
# 속성 초기화하는데 씀

# class Car:
#     def __init__(self, seats): # self는 초기화되고 있는 실제 객체
#         # initialise attributes
#         self.seats = seat

# seats = 5
# class Car:
#     def enter_race_mode(self):
#         self.seats = 2



# my_car.enter_race_mode()