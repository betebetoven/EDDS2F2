class bloque:
    def __init__(self) -> None:
        self.next = None
        self.bloque= {
            'index' : 0,
            'timestamp': 0,
            'nonce':0,
            'data':{
                'hash_prev':0,
                'merkle_root':0,
                'self_hash':0


            }




        }
