// Get references to the dropdown menus and containers
const firstDropdown = document.getElementById("first-dropdown");
const secondDropdownContainer = document.getElementById("second-dropdown-container");
const thirdDropdownContainer = document.getElementById("third-dropdown-container");
const numberInputContainer = document.getElementById("number-input")
const selectButton = document.getElementById("submit-button")

const basicFilters = ["Select an option","Bit Plane Slicing",'Power Transform','Image Threshold','Image Negative','Histogram Equalization']
const spatialFilters = ["Select an option","Smooth Filter","Sharp Filter","Min Filter","Max Filter","Median Filter","High Boost Filter"]
const frequencyFilters = ["Select an option","Low Pass","High Pass"]


let firstValue = 1
let secondValue = ""
let thirdValue = ""


function kernelSetter() {
    console.log("---------kernel setter")
    var numInput = document.createElement("INPUT");
                numInput.setAttribute("type", "range");
                numInput.setAttribute("name","num-Input");
                numInput.setAttribute("min","3");
                numInput.setAttribute("max","12");
                numInput.setAttribute("value","3");
                numInput.setAttribute("step","1")
               
                numInput.setAttribute("oninput","this.value")
        
                var showValue = document.createElement("output");
        
                numberInputContainer.appendChild(numInput)
                numberInputContainer.appendChild(showValue);
                showValue.innerText = numInput.value;
                numInput.setAttribute("oninput","this.nextElementSibling.innerText = this.value")
        
                numberValue = numInput.value

                return numberValue
    
  }


// Add event listener to the first dropdown menu
firstDropdown.addEventListener("change", () => {
    while(numberInputContainer.hasChildNodes()){
        numberInputContainer.removeChild(numberInputContainer.children[0]);
        console.log("Removing number slider 1")

      }


   

    // Remove any existing options from the second and third dropdown menus
    secondDropdownContainer.innerHTML = "";
    
  
    // Get the selected value from the first dropdown menu
    const selectedValue = firstDropdown.value;

    if (selectedValue === "1") {
        while(numberInputContainer.hasChildNodes()){
            numberInputContainer.removeChild(numberInputContainer.children[0]);
            console.log("Removing number slider Basic")

          }

        console.log("Basic Selected")
        firstValue = 1
        const secondDropdown = document.createElement("select");
        secondDropdown.setAttribute("name","second-dropdown");
        secondDropdown.setAttribute("class","form-select");
        //secondDropdown.classList.add("form-select");

        var options = [];

        
        for (index = 0; index < basicFilters.length; index++) {
            console.log(basicFilters[index]);
            options[index] = document.createElement("option");
            options[index].value = "1"+String.fromCharCode(65+index);
            console.log("1"+String.fromCharCode(65+index));
            options[index].textContent = basicFilters[index];
            secondDropdown.appendChild(options[index]);
        
        }


        secondDropdownContainer.appendChild(secondDropdown);
        

        secondDropdown.addEventListener("change",() => {
            while(numberInputContainer.hasChildNodes()){
                numberInputContainer.removeChild(numberInputContainer.children[0]);
                console.log("Removing number slider basic")
    
              }
            secondValue = secondDropdown.value

            if(secondValue === "1B"){
                console.log(basicFilters[1])

                //following line of code is to remove any other div set by other options
                while(numberInputContainer.hasChildNodes()){
                    numberInputContainer.removeChild(numberInputContainer.children[0]);

                  }

                  //the range of numbers that we want user to enter in case of bitplane slicing is 1-8
                  //we will add the number slider (range 0-8) 

                  var numInput = document.createElement("INPUT");
                    
                    numInput.setAttribute("type", "range");
                    numInput.setAttribute("name","num-Input");
                    numInput.setAttribute("min","0");
                    numInput.setAttribute("max","8");
                    numInput.setAttribute("value","5");
                    numInput.setAttribute("step","1")
                   
                    numInput.setAttribute("oninput","this.value")
            
                    var showValue = document.createElement("output");
            
                    numberInputContainer.appendChild(numInput)
                    numberInputContainer.appendChild(showValue);
                    showValue.innerText = numInput.value;
                    numInput.setAttribute("oninput","this.nextElementSibling.innerText = this.value")
            
                    numberValue = numInput.value

                

            }

            else if(secondValue === "1C"){
                console.log(basicFilters[2]);


                //following line of code is to remove any other div set by other options
                
                  while(numberInputContainer.hasChildNodes()){
                    numberInputContainer.removeChild(numberInputContainer.children[0]);

                  }
                  //the range of numbers that we want user to enter in case of power trasnform is 0-2 with the step size of 0.1
                  //we will add the number slider (range 0-8) 

                  var numInput = document.createElement("INPUT");
                    numInput.setAttribute("type", "range");
                    numInput.setAttribute("name","num-Input");
                    numInput.setAttribute("min","0");
                    numInput.setAttribute("max","2");
                    numInput.setAttribute("value","1.1");
                    numInput.setAttribute("step","0.1")
                   
                    numInput.setAttribute("oninput","this.value")
            
                    var showValue = document.createElement("output");
            
                    numberInputContainer.appendChild(numInput)
                    numberInputContainer.appendChild(showValue);
                    showValue.innerText = numInput.value;
                    numInput.setAttribute("oninput","this.nextElementSibling.innerText = this.value")
            
                    numberValue = numInput.value

            }

            else if(secondValue === "1D"){
                console.log(basicFilters[3]);

                //following line of code is to remove any other div set by other options
                
                while(numberInputContainer.hasChildNodes()){
                    numberInputContainer.removeChild(numberInputContainer.children[0]);

                  }
                  //the range of numbers that we want user to enter in case of Threshold is 10-240 with the step size of 1
                  //we will add the number slider (range 0-8) 

                  var numInput = document.createElement("INPUT");
                    numInput.setAttribute("type", "range");
                    numInput.setAttribute("name","num-Input");
                    numInput.setAttribute("min","10");
                    numInput.setAttribute("max","240");
                    numInput.setAttribute("value","150");
                    numInput.setAttribute("step","1")
                   
                    numInput.setAttribute("oninput","this.value")
            
                    var showValue = document.createElement("output");
            
                    numberInputContainer.appendChild(numInput)
                    numberInputContainer.appendChild(showValue);
                    showValue.innerText = numInput.value;
                    numInput.setAttribute("oninput","this.nextElementSibling.innerText = this.value")
            
                    numberValue = numInput.value

            }

            else if(secondValue === "1E"){
                console.log(basicFilters[4]);

                //following line of code is to remove any other div set by other options
                
                while(numberInputContainer.hasChildNodes()){
                    numberInputContainer.removeChild(numberInputContainer.children[0]);

                  }

                //We are not asking user to enter any number in case of Negative Image


            }

            else if(secondValue === "1F"){
                console.log(basicFilters[5]);
                //following line of code is to remove any other div set by other options
                
                while(numberInputContainer.hasChildNodes()){
                    numberInputContainer.removeChild(numberInputContainer.children[0]);

                  }

                //We are not asking user to enter any number in case of Histogram Equlization

            }

            else if(secondValue === '1A'){

                //following line of code is to remove any other div set by other options
                
                while(numberInputContainer.hasChildNodes()){
                    numberInputContainer.removeChild(numberInputContainer.children[0]);

                  }

            }


        })



    }
    else if (selectedValue === "2"){
        console.log("Spatial Filter Selected")
        while(numberInputContainer.hasChildNodes()){
            numberInputContainer.removeChild(numberInputContainer.children[0]);
            console.log("Removing number slider spatial")
    
          }
        
        firstValue = 2
        const secondDropdown = document.createElement("select");
        secondDropdown.setAttribute("name","second-dropdown");
        
        secondDropdown.setAttribute("class","form-select");
        secondDropdown.classList.add("form-select");

        var options = [];

        
        for (index = 0; index < spatialFilters.length; index++) {
            console.log(spatialFilters[index]);
            options[index] = document.createElement("option");
            options[index].value = "2"+String.fromCharCode(65+index);
            console.log("2"+String.fromCharCode(65+index));
            options[index].textContent = spatialFilters[index];
            secondDropdown.appendChild(options[index]);
        
        }


        secondDropdownContainer.appendChild(secondDropdown);
        secondDropdown.addEventListener("change",() => {
            secondValue = secondDropdown.value
            while(numberInputContainer.hasChildNodes()){
                numberInputContainer.removeChild(numberInputContainer.children[0]);
                console.log("Removing number slider Spatial")
    
              }
            if(secondValue !== '2A'){
                
    
                //following line of code is to remove any other div set by other options
                while(numberInputContainer.hasChildNodes()){
                    numberInputContainer.removeChild(numberInputContainer.children[0]);
                    console.log("Removing number slider Spatial inner")
    
                  }
    
                  //the range of numbers that we want user to enter in case of bitplane slicing is 1-8
                  //we will add the number slider (range 0-8) 
                  numberValue = kernelSetter()  
                  console.log("-------------"+secondValue)
                  console.log("-------------"+numberValue)

    
            }

            
        
        
        })



        
    }

    else if (selectedValue === "3"){
        console.log("Frequency filter selected")
        while(numberInputContainer.hasChildNodes()){
            numberInputContainer.removeChild(numberInputContainer.children[0]);
            console.log("Removing number slider ")
    
          }
        
        
        firstValue = 3
        const secondDropdown = document.createElement("select");
        secondDropdown.setAttribute("name","second-dropdown");
        secondDropdown.setAttribute("class","form-select");
        secondDropdown.classList.add("form-select");

        var options = [];

        
        for (index = 0; index < frequencyFilters.length; index++) {
            console.log(frequencyFilters[index]);
            options[index] = document.createElement("option");
            options[index].value = "3"+String.fromCharCode(65+index);
            console.log("3"+String.fromCharCode(65+index));
            options[index].textContent = frequencyFilters[index];
            secondDropdown.appendChild(options[index]);
        
        }


        secondDropdownContainer.appendChild(secondDropdown);


    }
})  