g++ -o Ejecutable main.cpp glove/glovehttpserver.cpp glove/glove.cpp glove/glovewebsockets.cpp glove/glovecoding.cpp glove/glovehttpcommon.cpp -lpthread -DENABLE_OPENSSL=0 -DENABLE_COMPRESSION=0 -std=c++11

