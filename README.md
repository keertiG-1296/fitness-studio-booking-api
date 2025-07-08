# fitness-studio-booking-api
Fitness Studio Booking API is a backend web service built using FastAPI, designed to help a fitness studio manage class schedules and allow clients to book spots in available classes.
**


**1. Tech Stack**
     - Backend
          FastAPI – High-performance Python web framework for building APIs
          Uvicorn – Lightning-fast ASGI server to run FastAPI
          Pydantic – Data validation and parsing using Python type hints
          SQLAlchemy – ORM (Object Relational Mapper) for interacting with the database
          SQLite – Lightweight, file-based relational database (used for local development)
          
    - Dev Tools
          Python 3.10+
          cURL or Postman – For testing API endpoints
          Swagger UI – Built-in API documentation at /docs
          Virtualenv – For isolated Python environment (optional but recommended)


**2. Project Setup Instructions****
   - Download the Project.It's on the Github
   - git clone https://github.com/keertiG-1296/fitness-studio-booking-api.git
   - Create a Virtual Environment (Recommended)
   - Install Dependencies
  
**3. Run Locally**
   - Activate the virtual enviornment [ If created]
   - uvicorn app.main:app --reload

**4. API Usage example**
    
    
    Step 1: Create a New Class [POST/classes]
            
            
            JSON Ex:
            
            {
                        "name": "Yoga Flow",
                        "dateTime": "2025-07-10T08:00:00Z",
                        "instructor": "Keerti",
                        "availableSlots": 20
                      }
          
           
           cURL: curl -X POST "http://127.0.0.1:8000/classes" \
                  -H "Content-Type: application/json" \
                  -d '{"name": "Yoga Flow", "dateTime": "2025-07-10T08:00:00Z", "instructor": "Keerti", "availableSlots": 20}'

  
  Step 2:  Get All Classes [GET /classes]
            
            
            cURL: curl "http://127.0.0.1:8000/classes"
            
            
            Sample Response: 
            
            [
                                {
                                "id": 1,
                               "name": "Yoga Flow",
                               "dateTime": "2025-07-10T08:00:00Z",
                               "instructor": "Keerti",
                                "availableSlots": 20
                               }
                                ]
  
   
   Step 3: Book a Class [POST /book]
            
            
            JSON Ex: 
            
            {
                      "class_id": 1,
                      "client_name": "John Doe",
                      "client_email": "john@example.com"
                    }
            
            
            cURL:
                  
                  
                  curl -X POST "http://127.0.0.1:8000/book" \
                  -H "Content-Type: application/json" \
                  -d '{"class_id": 1, "client_name": "John Doe", "client_email": "john@example.com"}'
   
   
   Step 4: View Bookings by Email
          
           
           GET /bookings?email=john@example.com
          
           
           cURL: curl "http://127.0.0.1:8000/bookings?email=john@example.com"
           
           
           Sample Response:
                           
                             
                             [
                                {
                                  "id": 1,
                                  "class_id": 1,
                                  "client_name": "John Doe",
                                  "client_email": "john@example.com"
                                }
                              ]


Example Error (No Available Slots)


{
  "detail": "No slots available"
}

                
