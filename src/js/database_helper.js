const { MongoClient } = require('mongodb');
class db_connect{
    constructor(){
        this.uri = "mongodb+srv://admin:CFREapp@cfre.1zs8dam.mongodb.net/?retryWrites=true&w=majority";
        this.client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });   
    }
    async connect(){
        try{
            this.db = this.client.db('CFRE');
            this.users = this.db.collection("Users"); 
        }catch(e){
            console.error("Database connection failed: ",e);
        }
    }
    async login(email, pwd){
        try{
            var query = {"email": email}
            var result =  await this.users.findOne(query);
            if(result){
                if(String(result.get("pwd")).localeCompare(pwd) == 0){
                    sessionStorage.setItem("user_name", result.get("name"));
                    sessionStorage.setItem("user_email", email);
                    return 0,"Login Successful";
                }
                return 1,"Password is incorrect";     
            }
            return 1,"Email is incorrect";
                    
        }catch(e){
            console.error("Login failed: ",e);
            return 1,"Login Failed";
        }
    }
    async signup(name, email, pwd){
        try{
            var query = {"email": email}
            var result =  await this.users.findOne(query);
            console.log(query);
            if(result){
                return 1,"Account already exists. Try Logging in";
            }
            var doc = {
                "name": name,
                "email": email,
                "pwd": pwd
            } 
            await this.users.insertOne(doc);
            sessionStorage.setItem("user_name", name);
            sessionStorage.setItem("user_email", email);
            return 0,"Signup Successful";
        }catch(e){
            console.error("Signup failed: ",e);
            return 1,"Signup Failed";
        }
    }
    async disconnect(){
        await this.client.close();
    }
}