# Littlelemon
## Capstone project for the meta backend course on coursera

### For the Reviewers: Please test the following endpoints. 
<p>
POST /restaurant/auth/token/login<br>  
	obtain acces token with basic authentication (payload formdata 'username', 'password')  <br>
GET /restaurant/auth/users/  <br>
GET /restaurant/auth/users/me/  <br>

Other djoser default endpoint are available at /restaurant/auth/  	
</p>
<p>	
GET /restaurant/menu/<br>  
list all menu items (**all the following require token authentication**)  <br>
GET /restaurant/menu/<pk>/  <br>
retrieve single menu item (with trailing slash!)  <br>
POST /restaurant/menu/  <br>
create item (payload formdata 'title', 'price', 'inventory')  <br>
PATCH /restaurant/menu/<pk>/  <br>
update single menu item (with trailing slash!)  <br>
DELETE /restaurant/menu/<pk>/  <br>
delete single menu item (with trailing slash!)  <br>
</p>
<p>
GET /restaurant/booking/  <br>
list all bookings  <br>
GET /restaurant/booking/<pk>/  <br>
retrieve a booking item  <br>
POST /restaurant/booking/  <br>
create a booking ('name', 'noofguests', 'bookingdate')  <br>
PATCH /restaurant/booking/<pk>/  <br>
update single menu item (with trailing slash!)  <br>
DELETE /restaurant/menu/<pk>/  <br>
delete single booking item (with trailing slash!) <br>
</p>	

#### N.B. test classes for views and models are included in one file "tests.py" 
