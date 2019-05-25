def incluindo_usuario(cursor, conn, nome, senha):
    cursor.execute(f'INSERT into encurtar.pessoas (nome,senha) VALUES ("{nome}","{senha}")')
    conn.commit()

