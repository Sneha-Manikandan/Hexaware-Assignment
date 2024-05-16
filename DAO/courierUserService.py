from Util.DBConn import DBConnection
from abc import ABC,abstractmethod



class ICourierUserService(ABC):
    @abstractmethod
    def placeOrder(self, courier_obj):
        pass

    @abstractmethod
    def getOrderStatus(self, tracking_number):
        pass

    @abstractmethod
    def cancelOrder(self, tracking_number):
        pass

    @abstractmethod
    def getAssignedOrder(self, courier_staff_id):
        pass

class CourierUserService(ICourierUserService,DBConnection):
    tracking_number=1239090765
    def trackingNumber():
        tracking_number+=1
        return str(tracking_number)
    def placeOrder(self,courier):
        self.cursor.execute("INSERT INTO Courier (CourierID,UserId, SenderName, SenderAddress, ReceiverName, ReceiverAddress, TrackingNumber) VALUES(?,?,?,?,?,?,?)",
                       (courier.courierID,courier.UserId,courier.SenderName,courier.SenderAddress,courier.ReceiverName,courier.trackingNumber)
                       )
        self.conn.commit()

    def display_order(self):
        try:
            self.cursor.execute("SELECT * FROM Courier")
            Couriers=self.cursor.fetchall()
            for courier in Couriers:
                print(courier)
        except Exception as e:
            print("Error!!",e)

    def getOrderStatus(self,TrackingNumber):
        try:
            self.cursor.execute("SELECT status FROM Courier WHERE TrackingNumber=?",
            (TrackingNumber)
            )
            courier_status=self.cursor.fetchone()
            print(courier_status)
        except Exception as e:
            print("Error!!",e)

    def cancelOrder(self,TrackingNumber):
        try:
            self.cursor.execute("Delete FROM CourierServiceMapping WHERE courierId IN (select courierId from courier where trackingNumber like ?",
                        (TrackingNumber)
                        )
            self.cursor.execute("Delete FROM EmployeeCourier WHERE courierId IN (select courierId from courier where trackingNumber like ?",
                        (TrackingNumber)
                        )
            self.cursor.execute("Delete FROM Payment WHERE courierId IN (select courierId from courier where trackingNumber like ?",
                        (TrackingNumber)
                        )
            self.cursor.execute("Delete FROM Courier WHERE TrackingNumber LIKE?",
                        (TrackingNumber)
                        )
        except Exception as e:
            print("Error !!!",e)
        
       
    def getAssignedOrder(self,employeeID):
        try:
            self.cursor.execute("SELECT CourierID FROM EmployeeCourier WHERE EmployeeID=?",
                        (employeeID) 
                        )
            couriers=self.cursor.fetchall()
            for courier in couriers:
                print(courier)
        except Exception as e:
            print("Error !!!",e)