const sqlite3 = require('sqlite3').verbose();

// open the database
let db = new sqlite3.Database('./political.db', sqlite3.OPEN_READWRITE, (err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Connected to the Political database.');
});
 
db.serialize(() => {
  db.each(`SELECT PlaylistId as id,
                  Name as name
           FROM playlists`, (err, row) => {
    if (err) {
      console.error(err.message);
    }
    console.log(row.id + "\t" + row.name);
  });
});
 
db.close((err) => {
  if (err) {
    console.error(err.message);
  }
  console.log('Close the database connection.');
});

function loadData(){
  name = "Nancy Pelosi222";
  image = "img/pelosi.jpg";
  email = "nancypelosi@dems.com";
  email_href = "mailto:nancypelosi@dems.com";
  link1 = "Official Link";
  link1_href = "https://www.yahoo.com";
  seat = "House Seat B";
  term = "4";
  address = "231 somewhere, CA 94605";
  mobtel = "555-555-5555";
  mobtel_tel = "tel:+555-555-5555";
  bio = "This is the bio loaded from JS"
}
//member = 
function data(){  
  loadData();
  document.getElementById("name").innerHTML = name;
  document.getElementById("image").src = image;
  document.getElementById("email").innerHTML = email;
    document.getElementById("email").href = email_href;
  document.getElementById("link1").innerHTML = link1;
  document.getElementById("link1").href = link1_href;
  document.getElementById("seat").innerHTML = seat;
  document.getElementById("term").innerHTML = term;
  document.getElementById("address").innerHTML = address;
  document.getElementById("mobtel").innerHTML = mobtel;
  document.getElementById("mobtel").href = mobtel_tel;
  document.getElementById("bio").innerHTML = bio;
}