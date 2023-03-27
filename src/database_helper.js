const {MongoClient} = require('mongodb');
class db_connect{
    async connect(){
        this.uri = "mongodb+srv://admin:CFREapp@cfre.1zs8dam.mongodb.net/?retryWrites=true&w=majority";
        this.client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });   
        try{
            this.db = this.client.db('CFRE');
            this.users = this.db.collection("Users"); 
        }catch(e){
            console.error("Database connection failed: ",e);
        }
        finally {
            await client.close();
        }
    }
    async login(){
        try{
            //Query goes here
        }catch(e){
            console.error("Login failed: ",e);
        }
        finally {
            await client.close();
        }
    }
}

export * from db_connect;
