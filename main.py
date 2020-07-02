from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

livros = [
    {
        "id": 1,
        "nome": "Amoras",
        "image": "https://images-na.ssl-images-amazon.com/images/I/51TCpYptizL._SY498_BO1,204,203,200_.jpg",
        "autor": "Aldo Fabrini",
        "paginas": "",
        "nota": "4.8/5",
        "tipo":"pdf",
        "compra":"https://www.amazon.com.br/dp/8574068365/ref=s9_acsd_hps_bw_c2_x_2_i?pf_rd_m=A3RN7G7QC5MWSZ&pf_rd_s=merchandised-search-6&pf_rd_r=ZV9DHPHPA8F0D1S90F0X&pf_rd_t=101&pf_rd_p=ed29da53-5931-4a7a-900e-1bb21e030b2f&pf_rd_i=7844001011"
    },
    {
        "id": 2,
        "nome": "O poder do hábito",
        "image": "https://images-na.ssl-images-amazon.com/images/I/51VFNJGBvqL._SX346_BO1,204,203,200_.jpg",
        "autor": "Charles Duhigg",
        "paginas": "",
        "nota": "4.7/5",
        "tipo":"pdf",
        "compra":"https://www.amazon.com.br/poder-do-h%C3%A1bito-Charles-Duhigg/dp/8539004119/ref=zg_bs_books_9?_encoding=UTF8&psc=1&refRID=FQ04Q6HA39W27CEYK1WE"
    },{
        "id": 3,
        "nome": "O Pequeno Príncipe Preto",
        "image": "https://images-na.ssl-images-amazon.com/images/I/41KF1iRHe4L._SX373_BO1,204,203,200_.jpg",
        "autor": "Rodrigo França",
        "paginas": "",
        "nota": "5/5",
        "tipo":"pdf",
        "compra":"https://www.amazon.com.br/Pequeno-Pr%C3%ADncipe-Preto-Rodrigo-Fran%C3%A7a/dp/8520938388/ref=pd_sbs_14_2/132-0412438-4892949?_encoding=UTF8&pd_rd_i=8520938388&pd_rd_r=472ed92d-e2e0-4a64-9a1d-0cf0ec8cb375&pd_rd_w=klIL3&pd_rd_wg=DTddt&pf_rd_p=27be8476-6095-40f6-b57d-3e82cf55061c&pf_rd_r=8N8Z46WM5VBQB69YSS06&psc=1&refRID=8N8Z46WM5VBQB69YSS06"
    },{
        "id": 4,
        "nome": "Meu crespo é de rainha",
        "image": "https://images-na.ssl-images-amazon.com/images/I/51u4iWzjufL._SX427_BO1,204,203,200_.jpg",
        "autor": "Bell Hooks",
        "paginas": "",
        "nota": "5/5",
        "tipo":"pdf",
        "compra":"https://www.amazon.com.br/Meu-Crespo-Rainha-Bell-Hooks/dp/857559608X/ref=pd_sbs_14_3/132-0412438-4892949?_encoding=UTF8&pd_rd_i=857559608X&pd_rd_r=472ed92d-e2e0-4a64-9a1d-0cf0ec8cb375&pd_rd_w=klIL3&pd_rd_wg=DTddt&pf_rd_p=27be8476-6095-40f6-b57d-3e82cf55061c&pf_rd_r=8N8Z46WM5VBQB69YSS06&psc=1&refRID=8N8Z46WM5VBQB69YSS06"
    },{
        "id": 5,
        "nome": "Amoras",
        "image": "https://images-na.ssl-images-amazon.com/images/I/51TCpYptizL._SY498_BO1,204,203,200_.jpg",
        "autor": "Aldo Fabrini",
        "paginas": "",
        "nota": "4.8/5",
        "tipo":"pdf",
        "compra":"https://www.amazon.com.br/dp/8574068365/ref=s9_acsd_hps_bw_c2_x_2_i?pf_rd_m=A3RN7G7QC5MWSZ&pf_rd_s=merchandised-search-6&pf_rd_r=ZV9DHPHPA8F0D1S90F0X&pf_rd_t=101&pf_rd_p=ed29da53-5931-4a7a-900e-1bb21e030b2f&pf_rd_i=7844001011"
    },{
        "id": 6,
        "nome": "Capitão Cueca",
        "image": "https://images-na.ssl-images-amazon.com/images/I/51TCpYptizL._SY498_BO1,204,203,200_.jpg",
        "autor": "Dav Pilkey",
        "paginas": "",
        "nota": "5/5",
        "tipo":"pdf",
        "compra":"https://www.amazon.com.br/Capit%C3%A3o-grande-desagrad%C3%A1vel-batalha-bi%C3%B4nico/dp/8574068837/ref=gbph_img_m-2_f06c_0584acbe?smid=A1ZZFT5FULY4LN&pf_rd_p=bd0de57a-f54b-4ad9-b752-233587c3f06c&pf_rd_s=merchandised-search-2&pf_rd_t=101&pf_rd_i=7844001011&pf_rd_m=A1ZZFT5FULY4LN&pf_rd_r=24JEW7S5B864A5JK28JJ"
    }
    
]


@app.get('/login')
async def login():
    return {"message": "hello"}


@app.get('/user/{id}')
async def userID(id: int):
    if id == 123:
        return {"user": {
            "id": "123",
            "name": "Wesley",
            "email":"wesleybenicio4@gmail.com",
            "perfilimg":"https://media.tenor.com/images/74a2b4b0fc38bc87c81f68b0bb24572d/tenor.gif"}}

@app.get('/books')
async def book():
    return livros
    
@app.get('/books/{id}')
async def books(id:int):
    if id:
        return livros[id]
        
