import string

class MaquinaTuringCesar:
    """
    Implementación de una Máquina de Turing Determinista (DTM) de una sola cinta
    diseñada como un Transductor para el Cifrado César Generalizado.
    
    Definición Formal: M = (Q, Sigma, Gamma, delta, q0, F)
    Donde:
        Q = {q_process, q_halt}
        Sigma = {A, B, ..., Z} (Alfabeto de entrada)
        Gamma = Sigma U {#} (Alfabeto de cinta, # es blanco)
        delta: Q x Gamma -> Q x Gamma x {L, R, S}
        q0 = q_process
        F = {q_halt}
    
    Complejidad Temporal: O(n), donde n es la longitud de la cadena. 
    La máquina recorre la cinta linealmente una sola vez de izquierda a derecha.
    """

    def __init__(self, clave_k: int):
        self.k = clave_k
        self.alfabeto = string.ascii_uppercase
        self.estado_actual = 'q_process'
        self.cinta = []
        self.cabezal = 0
        self.historial = [] # Para auditoría y visualización
        self.transiciones = self._generar_transiciones_dinamicas()

    def _generar_transiciones_dinamicas(self):
        """
        Genera la función delta (δ) basada en aritmética modular sobre Z_26.
        f(x) = (Pos(x) + K) mod 26
        """
        delta = {}
        n = len(self.alfabeto)
        
        # Reglas de transformación para cada caracter del alfabeto
        for char in self.alfabeto:
            idx_original = self.alfabeto.index(char)
            # Aplicamos la aritmética modular: (x + k) mod 26
            idx_cifrado = (idx_original + self.k) % n
            char_cifrado = self.alfabeto[idx_cifrado]
            
            # (Estado Actual, Lee) -> (Nuevo Estado, Escribe, Mueve)
            delta[('q_process', char)] = ('q_process', char_cifrado, 'R')

        # Regla de parada: Si lee vacío/blanco (#), se detiene
        delta[('q_process', '#')] = ('q_halt', '#', 'S')
        
        return delta

    def cargar_cinta(self, texto_entrada: str):
        """Inicializa la cinta con el texto sanitizado y un delimitador final."""
        self.cinta = list(texto_entrada) + ['#']
        self.cabezal = 0
        self.estado_actual = 'q_process'
        self.historial = []
        # Guardar estado inicial (Snapshot t=0)
        self._registrar_snapshot()

    def _registrar_snapshot(self):
        self.historial.append({
            'paso': len(self.historial),
            'estado': self.estado_actual,
            'cabezal': self.cabezal,
            'cinta': list(self.cinta)  # Copia profunda
        })

    def ejecutar(self):
        """Ejecuta la máquina paso a paso hasta alcanzar el estado de parada."""
        while self.estado_actual != 'q_halt':
            simbolo_leido = self.cinta[self.cabezal]
            clave_transicion = (self.estado_actual, simbolo_leido)

            if clave_transicion in self.transiciones:
                nuevo_estado, simbolo_escribir, movimiento = self.transiciones[clave_transicion]
                
                # Acciones de la MT
                self.cinta[self.cabezal] = simbolo_escribir
                self.estado_actual = nuevo_estado
                
                if movimiento == 'R':
                    self.cabezal += 1
                elif movimiento == 'L':
                    self.cabezal -= 1
                
                self._registrar_snapshot()
            else:
                raise Exception(f"Transición no definida para: {clave_transicion}")
        
        return "".join(self.cinta).replace('#', '')

    def obtener_historial(self):
        return self.historial