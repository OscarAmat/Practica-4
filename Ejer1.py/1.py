import requests

def precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
  
    while True:
        try:
            cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
            break 
        except ValueError:
            print("Vuelva a ingresarlo.")

   
    el_precio_bitcoin = precio_bitcoin()

    if el_precio_bitcoin is not None:
       
        costo_usd = cantidad_bitcoins * el_precio_bitcoin

      
        print(f"{cantidad_bitcoins:.4f} bitcoins es: ${costo_usd:,.4f}")

if __name__ == "__main__":
    main()
