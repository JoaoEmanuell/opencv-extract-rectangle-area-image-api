- [Extrair](#extrair)
  - [Retângulo não encontrado](#retângulo-não-encontrado)
  - [Imagem inválida](#imagem-inválida)


# Extrair

O retângulo vermelho deve estar entre as cores #FF0000 [RGB(255, 000, 000)] e #F00000 [RGB(240, 000, 000)], caso contrário a extração irá falhar.

Para fazer a extração do retângulo vermelho da imagem, acesse a rota */extract* usando o método **POST**.

Faça o upload da imagem e aguarde o retorno.

Exemplo:

    url = 'endpoint'
    image = f'{BASE_DIR}/assets/example_image_with_red_rectangle.png'

Abra a imagem

    with open(image, 'rb') as image_file:

Envie para a rota, envie a imagem usando o *files* e configure um tempo de expiração de 60 segundos.

    response = post(f'{url}/extract', files={
        "file": image_file
    }, timeout=60)

Após isso converta a resposta para um json.

    json = response.json()

Ele irá conter as coordenadas do maior retângulo vermelho da imagem.

    {
        'x': 85, 
        'y': 16, 
        'h': 165,
        'w': 140
    }

## Retângulo não encontrado

Caso ele não encontre o retângulo, o retorno será o seguinte:

    {
        'msg': 'Error to extract the rectangle'
    }

## Imagem inválida

Caso a imagem enviada não seja válida, o retorno será o seguinte:

    {
        'msg': 'Image not valid'
    }