

// ------- SALES HISTORY ------------ 
function exportToExcel(tableID, filename = ''){
    var downloadurl;
    var dataFileType = 'application/vnd.ms-excel';
    var tableSelect = document.getElementById(tableID);
    var tableHTMLData = tableSelect.outerHTML.replace(/ /g, '%20');
    
    filename = filename?filename+'.xls':'saleshistory.xls';
    
    downloadurl = document.createElement("a");
    
    document.body.appendChild(downloadurl);
    
    if(navigator.msSaveOrOpenBlob){
        var blob = new Blob(['\ufeff', tableHTMLData], {
            type: dataFileType
        });
        navigator.msSaveOrOpenBlob( blob, filename);
    }else{
        downloadurl.href = 'data:' + dataFileType + ', ' + tableHTMLData;
    
        downloadurl.download = filename;
        
        downloadurl.click();
    }
}

/****inventory */
function invt()
{
    var ItemName = document.getElementById("ItemName");
    var ItemQuantity = document.getElementById("ItemQuantity");
    
    if(ItemQuantity.value <= "0" || ItemQuantity.value == "")
    {
        alert ("**Invalid Input**" )
    }
    else if(ItemName.value == "") 
    {
        alert ("**Enter Item Name**" )
    }
    else 
    {
        alert ("**Item added successfully!**")
    }
}

function updt()
{
    var itemQuantity = document.getElementById("Item_Quantity");

    if(itemQuantity.value <= "0" || itemQuantity.value == "")
    {
        alert ("**Invalid Input**" )
    }
    else 
    {
        alert ("**Item updated successfully!**")
    }
}

function rm()
{
    var itemquantity = document.getElementById("itemquantity");

    if(itemquantity.value <= "0" || itemquantity.value == "")
    {
        alert ("**Invalid Input**" )
    }
    else 
    {
        alert ("**Room price updated successfully!**")
    }
}

// ------- LOGOUT ----------
function logout () {
    if (confirm("Are you sure you want to logout?") == true){
      window.close()
    } else {
      pass
    }
  }
