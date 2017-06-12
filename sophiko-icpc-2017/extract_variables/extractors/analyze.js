var fs = require('fs');
var esprima = require('esprima');

function dumpVariables(block) {
    
    //Dumping all the variable declarations in the block, if they exist
    if (block.type === 'VariableDeclaration') {
        for (var i=0; i<block.declarations.length; i++) {
            var decl = block.declarations[i];
            console.log(decl.id.name);   
        }
    }

    //Going over all the keys in the block
    var keys = Object.keys(block);
    for (var keyIdx=0; keyIdx<keys.length; keyIdx++) { 

        //Getting the key and the value
        var key = keys[keyIdx];
        var value = block[key];

        if (!(value instanceof Object)) {
            continue; //This isn't an object - skip it
        }

        //Recursively dumping each internal block
        if (value.length) {
            //This is an array
            for (var i=0; i<value.length; i++)
                dumpVariables(value[i]);
        }
        else
            dumpVariables(value);
   }
}

function analyzeCode(code) {

    //Getting the AST for this source file
    var ast = esprima.parse(code);

    //Going over each variable declaration and dumping it
    dumpVariables(ast)
}

//Making sure the filename is supplied
if (process.argv.length < 3) {
    console.log('Usage: analyze.js file.js');
    process.exit(1);
}

//Dumping the variable declarations from the given source file
var filename = process.argv[2];
var code = fs.readFileSync(filename);
analyzeCode(code);

