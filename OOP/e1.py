class Person():
    #constructor
    def __init__(self,name='',age=0,dni=''):
        self.name = name
        self.age = age
        self.dni = dni #private attribute
    #get
    @property
    def getName(self):
        return self.__name
    @property
    def getAge(self):
        return self.__age
    @property
    def getDNI(self):
        return self.__dni

    #set
    @name.setter
    def name(self,name):
        self.__name=name
    @age.setter
    def age(self,age):
        self.__age = age
    @dni.setter
    def dni(self,dni):
        self.__dni = dni 


person = Person()
person.setName('roberto')
person.setAge(19)
person.setDNI('JHVGDAWUYV')

print(person.dni)