document.addEventListener("DOMContentLoaded",()=>{
    const form=document.getElementById("employeeForm");
    form.addEventListener("submit",async(event)=>{
        event.preventDefault();
        //get values from the input fields 
        const name=document.getElementById("name").value;
        const email=document.getElementById("email").value;
        const department=document.getElementById("department").value;
        const salary=document.getElementById("salary").value;
        //create a javascript object to send to the backend .
        const newEmployee={
            name:name,
            email:email,
            department:department,
            salary:parseFloat(salary)
        };
        try{
            const response=await fetch("http://127.0.0.1:8000/employees",{
                method:"POST",
                headers:{
                    "Content-Type":"application/json"
                },
                body:JSON.stringify(newEmployee)
            });
            if(response.ok){
                const addedEmp=await response.json();
                alert("✅ Employee added successfully with ID: "+addedEmp.id);
                form.reset();//clear the form after sucessfull post 
            }
            else{
                alert("❌failed to add employee.");
                
            }
        }catch(error){
            console.error("Error",error);
            alert("❌error adding employee");
        }
        
    });
});