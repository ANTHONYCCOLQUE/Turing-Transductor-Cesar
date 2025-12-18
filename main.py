import re
import csv
import sys
import os
from maquina_turing import MaquinaTuringCesar
from visualizador import VisualizadorTuring

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def sanitizar_entrada(texto):
    """
    Ingeniería de Software: Sanitización estricta.
    Elimina cualquier caracter que no pertenezca al grupo cíclico Z_26 (A-Z).
    """
    texto_limpio = re.sub(r'[^A-Z]', '', texto.upper())
    return texto_limpio

def exportar_csv(historial, filename="auditoria_turing.csv"):
    """Exporta la trazabilidad completa para análisis posterior."""
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Paso", "Estado", "Pos_Cabezal", "Contenido_Cinta"])
            
            for h in historial:
                cinta_str = "".join(h['cinta'])
                writer.writerow([h['paso'], h['estado'], h['cabezal'], cinta_str])
        print(f"   [+] Trazabilidad exportada a: {filename}")
    except IOError as e:
        print(f"   [!] Error al exportar CSV: {e}")

def main():
    while True:
        limpiar_pantalla()
        print("=================================================")
        print("   SIMULADOR DE MÁQUINA DE TURING - CESAR (Z26)")
        print("=================================================")
        print("1. Configurar Nueva Máquina y Ejecutar")
        print("2. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == '2':
            print("Saliendo del sistema...")
            sys.exit()
            
        if opcion == '1':
            try:
                # 1. Configuración (Input K)
                k_input = input("Ingrese la clave de desplazamiento K (entero): ")
                if not k_input.isdigit():
                    raise ValueError("La clave debe ser un número entero.")
                k = int(k_input)
                
                # 2. Input Texto
                raw_text = input("Ingrese el mensaje (A-Z): ")
                texto_procesado = sanitizar_entrada(raw_text)
                
                if not texto_procesado:
                    print("\n[!] Error: El texto no contiene caracteres válidos (A-Z).")
                    input("Presione Enter para continuar...")
                    continue

                print(f"\n--- Iniciando Procesamiento ---")
                print(f"Texto Entrada (Sanitizado): {texto_procesado}")
                print(f"Clave K: {k}")

                # 3. Instanciación y Ejecución del Modelo
                mt = MaquinaTuringCesar(clave_k=k)
                mt.cargar_cinta(texto_procesado)
                resultado = mt.ejecutar()
                historial = mt.obtener_historial()

                print(f"\n[OK] Ejecución Finalizada.")
                print(f"Resultado en Cinta: {resultado}")

                # --- 4. AUDITORÍA DE CALIDAD (INTEGRIDAD) ---
                # Validamos que la función sea biyectiva intentando revertirla
                print("\n--- Auditoría de Calidad del Algoritmo ---")
                
                # Cálculo de la inversa modular en Z26: (26 - K) % 26
                k_inversa = (26 - k) % 26
                
                # Instanciamos una segunda máquina "Auditora"
                mt_auditor = MaquinaTuringCesar(clave_k=k_inversa)
                mt_auditor.cargar_cinta(resultado) # Cargamos el resultado cifrado
                resultado_auditado = mt_auditor.ejecutar()
                
                if resultado_auditado == texto_procesado:
                    print(f" ✅ TEST DE INTEGRIDAD: EXITOSO")
                    print(f"     La transformación es reversible (Propiedad Biyectiva).")
                    print(f"     Decodificación MT(-{k}): '{resultado}' -> '{resultado_auditado}'")
                else:
                    print(f" ❌ FALLO DE INTEGRIDAD")
                    print(f"     Error: No se pudo recuperar el mensaje original.")

                # 5. Generación de Vistas (Reportes)
                print("\n--- Generando Artefactos ---")
                VisualizadorTuring.generar_diagrama_estados(k)
                VisualizadorTuring.generar_heatmap_cinta(historial)
                exportar_csv(historial)

            except ValueError as ve:
                print(f"\n[!] Error de Validación: {ve}")
            except Exception as e:
                print(f"\n[!] Error Crítico del Sistema: {e}")
            
            input("\nPresione Enter para volver al menú principal...")

if __name__ == "__main__":
    main()