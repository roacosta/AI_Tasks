import math
def batches(batchTamanho, features, labels):
    
    assert len(features) == len(labels)
    #Aqui verifica se o tamanho de features é o mesmo que o tamanho das labels, se não, lança uma exceção e o programa é encerado.
    
    batchesRetorno = []
    
    tamanho = len(features)
    
    for i in range(0, tamanho, batchTamanho):
        j = i + batchTamanho
        batch = [features[i:j], labels[i:j]] # pega da posição i até a j
        batchesRetorno.append(batch)
        
    return batchesRetorno


