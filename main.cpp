#include "./glove/glovehttpserver.hpp"
#include "json/json.h"
#include <iostream>
#include<fstream>
#include <chrono>
#include <thread>
#include <string>
#include <vector>
#include "./glove/json.hpp"
#include "codigo/ListaSimple.cpp"
#include "List.h"
#include "nodo.h"
#include "ArbolB.h"
//HOOLAAA SI FUNCIONA ESTA MAMADAAAAAAAAAAA
List <Json::Value>usuarios_glob;
    /*List <Json::Value>articulos_glob;
    List <Json::Value>movimientos_glob;
    List <Json::Value>categoria;
    List<Json::Value>tut_global;*/
    ArbolB<Json::Value> usuariosB_glob;
   // Node<Json::Value> *cuenta;
int atoi(std::string s)
{
    try
    {
        return std::stod(s);
    }
    catch (std::exception &e)
    {
        return 0;
    }
}

static std::string jsonkv(std::string k, std::string v)
{
    /* "k": "v" */
    return "\"" + k + "\": \"" + v + "\"";
}

class Servidor
{
public:
    Servidor()
    {
        pruebas.InsertarEnOrden(100);
        pruebas.InsertarEnOrden(300);
        pruebas.InsertarEnOrden(200);
    }

    void get(GloveHttpRequest &request, GloveHttpResponse &response)
    {
        response.contentType("text/json");
        if (request.special["Id"].empty())
            response << pruebas.getDatos();
        else
        {
            response << "{ "
                     << jsonkv("status", "ok") << ",\n"
                     << jsonkv("Id_buscado", pruebas.Buscar(atoi(request.special["Id"]))) << " }";
        }
    }

    void post(GloveHttpRequest &request, GloveHttpResponse &response)
    {
        pruebas.InsertarEnOrden(atoi(request.special["Id"]));
        response << "{ "
                 << jsonkv("status", "ok") << ",\n"
                 << jsonkv("Id_nuevo", request.special["Id"]) << " }";
    }

private:
    ListaSimple pruebas;
};

int main(int argc, char *argv[])
{
     ifstream file("example.json");//volve a cambair a f1_masiva
    Json::Value actualJson;
    Json::Reader reader;
    reader.parse(file,actualJson);
    for (Json::Value objeto : actualJson["usuarios"]) {
        usuarios_glob.insert(objeto);
        usuariosB_glob.insertar(objeto);
        cout << objeto << endl;
    }
    usuariosB_glob.Grafo();



    Servidor cine;

    GloveHttpServer serv(8080, "", 2048);
    serv.compression("gzip, deflate");
    namespace ph = std::placeholders;
    serv.addRest("/Lista/$Id", 1,
                 GloveHttpServer::jsonApiErrorCall,
                 std::bind(&Servidor::get, &cine, ph::_1, ph::_2),
                 std::bind(&Servidor::post, &cine, ph::_1, ph::_2));
    std::cout << "Servidor en Ejecucion" << std::endl;
    while (1)
    {
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    std::cout << "TEST" << std::endl;
}
