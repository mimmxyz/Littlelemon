# Littlelemon
Capstone project for the meta backend course on coursera


For the Reviewers:Please test the following endpoints. 

POST /restaurant/auth/token/login
	obtain acces token with basic authentication (payload formdata 'username', 'password')
GET /restaurant/auth/users/
GET /restaurant/auth/users/me/

Other djoser default endpoint are available at /restaurant/auth/	
	
	
GET /restaurant/menu/
	list all menu items (all the following require token authentication)
GET /restaurant/menu/<pk>/
	retrieve single menu item (with trailing slash!)
POST /restaurant/menu/
	create item (payload formdata 'title', 'price', 'inventory')
PATCH /restaurant/menu/<pk>/
	update single menu item (with trailing slash!)
DELETE /restaurant/menu/<pk>/
	delete single menu item (with trailing slash!)

GET /restaurant/booking/
	list all bookings
GET /restaurant/booking/<pk>/
	retrieve a booking item
POST /restaurant/booking/
	create a booking ('name', 'noofguests', 'bookingdate')
PATCH /restaurant/booking/<pk>/
	update single menu item (with trailing slash!)
DELETE /restaurant/menu/<pk>/
	delete single booking item (with trailing slash!)
	
