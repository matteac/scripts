let string = "lorem lorem LoReM ipsum dolor sit amet consectetur adipisicing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua";

const normalize = string => string.toLowerCase().split(" ").join("");

const wordRep = (obj) => {
    let dict = {};
    let separateWords = obj.split(" ");
    for(let word of separateWords){
        if(normalize(word) in dict){
            ++dict[normalize(word)];
        }else{
            dict[normalize(word)] = 1;
        }
    } 
    return dict;
}


console.log(wordRep(string));