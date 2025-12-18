import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

class VisualizadorTuring:
    @staticmethod
    def generar_diagrama_estados(k, filename="turing_grafo.png"):
        """
        Genera el grafo dirigido de la arquitectura de la máquina.
        Simplifica la visualización agrupando transiciones para evitar saturación.
        """
        G = nx.DiGraph()
        
        # Definir nodos
        G.add_node("q_process", color='lightblue', style='filled', shape='circle')
        G.add_node("q_halt", color='lightgrey', style='filled', shape='doublecircle')
        
        # Definir aristas (Transiciones)
        # Nota: Representamos las 26 transiciones como una sola etiqueta lógica para claridad visual
        etiqueta_bucle = f"Σ -> Σ'\n(x + {k}) mod 26"
        G.add_edge("q_process", "q_process", label=etiqueta_bucle)
        G.add_edge("q_process", "q_halt", label="# -> #, S")
        
        pos = nx.spring_layout(G)
        plt.figure(figsize=(8, 6))
        
        # Dibujar nodos y aristas
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color=['lightblue', 'lightgrey'], 
                font_weight='bold', arrowsize=20)
        
        # Dibujar etiquetas de aristas
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
        
        plt.title(f"Arquitectura de Estados Finitos (Cifrado K={k})")
        plt.savefig(filename)
        plt.close()
        print(f"   [+] Diagrama de estados guardado en: {filename}")

    @staticmethod
    def generar_heatmap_cinta(historial, filename="turing_cinta_evolucion.png"):
        """
        Crea una matriz visual (Heatmap/Tabla) mostrando cómo cambia la cinta paso a paso.
        Resalta la posición del cabezal en cada paso.
        """
        pasos = len(historial)
        longitud_cinta = len(historial[0]['cinta'])
        
        # Preparar datos para la tabla
        cell_text = []
        cell_colors = []
        
        for step_data in historial:
            fila_texto = step_data['cinta']
            fila_color = ["#ffffff"] * longitud_cinta # Blanco por defecto
            
            # Resaltar la posición del cabezal (Amarillo)
            head_pos = step_data['cabezal']
            if head_pos < longitud_cinta:
                fila_color[head_pos] = "#ffff99"
                
            cell_text.append(fila_texto)
            cell_colors.append(fila_color)

        # Crear figura
        fig, ax = plt.subplots(figsize=(longitud_cinta * 0.8, pasos * 0.5 + 1))
        ax.axis('off')
        ax.axis('tight')
        
        # Crear la tabla
        tabla = ax.table(cellText=cell_text,
                         cellColours=cell_colors,
                         rowLabels=[f"t={i}" for i in range(pasos)],
                         colLabels=[f"Idx {i}" for i in range(longitud_cinta)],
                         loc='center',
                         cellLoc='center')
        
        tabla.auto_set_font_size(False)
        tabla.set_fontsize(10)
        tabla.scale(1, 1.5)
        
        plt.title("Matriz de Evolución de la Cinta (Traza de Ejecución)", pad=20)
        plt.savefig(filename, bbox_inches='tight', dpi=150)
        plt.close()
        print(f"   [+] Matriz de evolución guardada en: {filename}")