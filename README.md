# Slim Triton HTTP Client

A simplified python http client library and utilities for communicating with Triton Inference Server (based on tritonclient from NVIDIA)


This is a simplified implemetation of the triton client from NVIDIA, it is mainly made for running in the web browser with pyodide.
It only implement the http client, and most of the API remains the same but changed into async.

To install it, run `pip install tritonclient-slim`

You can find the official [client examples](https://github.com/triton-inference-server/client/tree/main/src/python/examples) demonstrate how to use the 
package to issue request to [triton inference server](https://github.com/triton-inference-server/server). However, please notice that you will need to
change the http client code into async style. For example, instead of doing `client.infer(...)`, you need to do `await client.infer(...)`.