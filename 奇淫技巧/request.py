import requests

#test
def foo1():
    response = requests.get("http://www.baidu.com")
    print(type(response))
    print(response.status_code)
    print(type(response.text))
    print(len(response.text))
    print(response.cookies)
    
#直接在url后面加参数
def foo2():
    response = requests.get("http://httpbin.org/get?name=Tom&age=20")
    print(response.text)
    
#用字典构造参数
def foo3():
    data = {
            "name" : "Tom",
            "age"  : "20"
    }
    headers = {"User-Agent" : "127.0.0.1"}
    response = requests.get("http://httpbin.org/get", params = data, headers = headers)
    print(response.text)
    
#解析json
def foo4():
    import json
    response = requests.get("http://httpbin.org/get")
    print(type(response.text))
    print("\n" + str(type(response.json())))
    print(response.json())
    print("\n" + str(type(json.loads(response.text))))
    print(json.loads(response.text))
    
#保存二进制文件
def foo5():
    response = requests.get("https://github.com/favicon.ico")
    print(type(response.text))
    print(type(response.content))
    print
    
if __name__ == "__main__":
    #foo1();
    #foo2();
    #foo3();
    foo4();