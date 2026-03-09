model_mapping_dict = {
    'Apple': {
        'classes': ['Apple Scab', 'Black Rot', 'Cedar Apple Rust', 'Healthy'],
        'model_path': 'apple_model.h5'
    },
    'Cherry': {
        'classes': ['Healthy', 'Powdery Mildew'],
        'model_path': 'cherry_model.h5'
    },
    'Corn': {
        'classes': ['Common Rust', 'Gray Leaf Spot', 'Healthy', 'Northern Leaf Blight'],
        'model_path': 'corn_model.h5'
    },
    'Grape': {
        'classes': ['Black Rot', 'Esca', 'Healthy', 'Leaf Blight'],
        'model_path': 'grape_model.h5'
    },
    'Peach': {
        'classes': ['Bacterial Spot', 'Healthy'],
        'model_path': 'peach_model.h5'
    },
    'Pepper': {
        'classes': ['Bacterial Spot', 'Healthy'],
        'model_path': 'pepper_model.h5'
    },
    'Potato': {
        'classes': ['Early Blight', 'Healthy', 'Late Blight'],
        'model_path': 'potato_model.h5'
    },
    'Strawberry': {
        'classes': ['Healthy', 'Leaf Scorch'],
        'model_path': 'strawberry_model.h5'
    },
    'Tomato': {
        'classes': ['Bacterial Spot', 'Early Blight', 'Healthy', 'Late Blight'],
        'model_path': 'tomato_model.h5'
    }
}

plant_disease_dict = {
    'Healthy': {
        'Description': '*A healthy plant exhibits vigorous growth and has no visible signs of disease or pest infestation. The leaves are typically green and free from discoloration, spots, or lesions. The stems are firm and erect, and the overall plant appearance is robust.*',
        'Symptoms': '*No symptoms; plant appears normal and free from any abnormalities.*',
        'Treatment': '*No treatment is required for a healthy plant. However, proper cultural practices such as adequate watering, fertilization, and pest management can help maintain plant health.*'
    },
    'Apple': {
        'Apple Scab': {
            'Description': '*Apple scab is a fungal disease that causes dark, scabby marks on the leaves and fruit of apple and crabapple trees. It is caused by the fungus Venturia inaequalis, which spreads by airborne spores and survives the winter on fallen leaves.*',
            'Symptoms': '*Small, brown or olive-green spots on the underside of young leaves, or on either side of older leaves.*',
            'Treatment': '*To control apple scab, practice good sanitation by removing fallen leaves and fruit from the ground. Apply fungicides as directed.*'
        },
        'Black Rot': {
            'Description': '*Black rot is a disease caused by the fungus Botryosphaeria obtusa that affects apple trees. It can cause reduced fruit productivity and quality, and can weaken the tree.*',
            'Symptoms': '*Small purple spots that develop into brownish-tan centers with darker margins and a purple outline, giving the leaves a "frog-eye" appearance.*',
            'Treatment': '*To control black rot, prune infected branches and remove and destroy infected fruit. Apply fungicides during the growing season.*'
        },
        'Cedar Apple Rust': {
            'Description': '*Cedar apple rust is a fungal disease that affects apple and cedar trees. It is caused by the fungus Gymnosporangium juniperi-virginianae, which requires both apple and cedar trees to complete its life cycle. The disease appears as orange or yellow spots on the leaves and fruit of apple trees.*',
            'Symptoms': '*Orange or yellow spots on the leaves and fruit. The spots may enlarge and develop a reddish-brown color. Spore-producing structures called telia may also form on the underside of the leaves.*',
            'Treatment': '*To control cedar apple rust, remove and destroy infected plant material. Prune nearby cedar trees to reduce spore production. Apply fungicides as directed.*'

        }
    },
    'Cherry': {
        'Powdery Mildew': {
            'Description': '*Powdery mildew is a fungal disease that affects cherry trees. It appears as white, powdery spots on the leaves and shoots. The disease is caused by various species of fungi from the Erysiphaceae family, which thrive in humid conditions.*',
            'Symptoms': '*White, powdery spots on the upper surfaces of leaves, shoots, and sometimes fruit. Infected leaves may become distorted or yellowed. Severe infections can cause premature leaf drop and reduced fruit quality.*',
            'Treatment': '*To control powdery mildew, remove and destroy infected plant material. Apply fungicides labeled for powdery mildew control, following label instructions carefully. Improve air circulation around plants by pruning and spacing trees appropriately.*'
        }

    },
    'Corn': {
        'Common Rust': {
            'Description': '*Common rust is a fungal disease caused by the pathogen Puccinia sorghi that affects corn plants. It appears as small, reddish-brown pustules on the leaves, stems, and husks of corn plants. The disease is favored by warm temperatures and high humidity.*',
            'Symptoms': '*Small, reddish-brown pustules on the upper surfaces of corn leaves. As the disease progresses, the pustules may coalesce, leading to widespread discoloration and weakening of the affected plant tissues.*',
            'Treatment': '*To control common rust, plant resistant corn varieties when available. Practice good crop rotation to reduce disease pressure. Apply fungicides if necessary, especially during periods of high disease pressure.*'
        },

        'Gray Leaf Spot': {
            'Description': '*Gray leaf spot is a fungal disease caused by the pathogen Cercospora zeae-maydis that affects corn plants. It appears as small, rectangular lesions with tan centers and dark brown to purple margins on the leaves. The disease thrives in warm, humid conditions and can spread rapidly in dense plantings.*',
            'Symptoms': '*Small, rectangular lesions with tan centers and dark brown to purple margins on the leaves. Lesions may coalesce, leading to large areas of blighted tissue. Severe infections can cause premature leaf death and yield loss.*',
            'Treatment': '*To control gray leaf spot, plant resistant corn varieties when available. Practice good crop rotation to reduce disease pressure. Apply fungicides preventatively, especially during periods of warm, humid weather and dense plantings.*'
        },

        'Northern Leaf Blight': {
            'Description': '*Northern leaf blight is a fungal disease caused by the pathogen Exserohilum turcicum that affects corn plants. It appears as large, cigar-shaped lesions with tan centers and dark brown to gray margins on the leaves. The disease thrives in warm, humid conditions and can spread rapidly under favorable weather conditions.*',
            'Symptoms': '*Large, cigar-shaped lesions with tan centers and dark brown to gray margins on the leaves. Lesions may start near the base of the plant and progress upward. Severe infections can cause significant leaf blighting and yield loss.*',
            'Treatment': '*To control northern leaf blight, plant resistant corn varieties when available. Practice good crop rotation to reduce disease pressure. Apply fungicides preventatively, especially during periods of warm, humid weather and dense plantings.*'
        }

    },
    'Grape': {
        'Black Rot': {
            'Description': '*Black rot is a fungal disease caused by the pathogen Guignardia bidwellii that affects grapevines. It appears as black, necrotic lesions on the leaves, shoots, and fruit. The disease thrives in warm, humid conditions and can spread rapidly in vineyards with poor air circulation.*',
            'Symptoms': '*Black, necrotic lesions on the leaves, shoots, and fruit. Lesions may expand and coalesce, leading to widespread blighting of the affected plant parts. Infected fruit may shrivel and become mummified.*',
            'Treatment': '*To control black rot, remove and destroy infected plant material. Practice good vineyard management, including proper pruning, spacing, and trellising to improve air circulation. Apply fungicides preventatively, especially during periods of warm, humid weather and susceptible growth stages.*'
        },

        'Esca': {
            'Description': '*Esca is a complex of fungal diseases affecting grapevines. It includes several different disorders, such as young vine decline, esca proper, and grapevine leaf stripe disease. These diseases cause various symptoms, including leaf discoloration, shoot dieback, and internal wood necrosis.*',
            'Symptoms': '*Symptoms of esca can vary depending on the specific disorder within the complex. Common symptoms include yellow or reddish-brown discoloration of leaves, internal wood necrosis in the trunk and cordons, and shoot dieback. The characteristic "tiger-striped" pattern may also appear on leaves.*',
            'Treatment': '*Management of esca is challenging due to its complexity and variability. Cultural practices such as pruning, canopy management, and irrigation can help reduce disease pressure. Application of fungicides may provide some control, but their efficacy can be limited.*'
        },


        'Leaf Blight': {
            'Description': '*Leaf blight is a fungal disease caused by various pathogens that affect grapevines. It appears as brown, necrotic lesions on the leaves, often surrounded by a yellow halo. The disease can lead to defoliation and reduced fruit quality if left uncontrolled.*',
            'Symptoms': '*Brown, necrotic lesions on the leaves, often with a yellow halo around the edges. Lesions may coalesce and cover large portions of the leaf surface. Severe infections can cause defoliation and weaken the vine.*',
            'Treatment': '*To control leaf blight, remove and destroy infected plant material. Practice good vineyard management, including proper pruning, spacing, and trellising to improve air circulation. Apply fungicides preventatively, especially during periods of warm, humid weather and susceptible growth stages.*'
        }


    },
    'Peach': {
        'Bacterial Spot': {
            'Description': '*Bacterial spot is a common bacterial disease affecting peach trees. It is caused by the bacterium Xanthomonas arboricola pv. pruni and can cause significant damage to leaves, fruit, and shoots. The disease is favored by warm, humid conditions and can spread rapidly during wet weather.*',
            'Symptoms': '*Symptoms of bacterial spot include small, water-soaked lesions on the leaves, which later turn brown and may have a yellow halo. Lesions on the fruit may appear as small, raised spots with a water-soaked appearance. Severe infections can cause defoliation and fruit loss.*',
            'Treatment': '*To control bacterial spot, practice good sanitation by removing and destroying infected plant material. Apply copper-based fungicides or bactericides as directed, especially during periods of high disease pressure. Prune trees to improve air circulation and reduce disease spread.*'
        }

    },
    'Pepper': {
        'Bacterial Spot': {
            'Description': '*Bacterial spot is a common bacterial disease affecting pepper plants. It is caused by the bacterium Xanthomonas campestris pv. vesicatoria and can cause significant damage to leaves, fruit, and stems. The disease is favored by warm, humid conditions and can spread rapidly during wet weather.*',
            'Symptoms': '*Symptoms of bacterial spot include small, water-soaked lesions on the leaves, which later turn brown and may have a yellow halo. Lesions on the fruit may appear as small, raised spots with a water-soaked appearance. Severe infections can cause defoliation and fruit loss.*',
            'Treatment': '*To control bacterial spot, practice good sanitation by removing and destroying infected plant material. Apply copper-based fungicides or bactericides as directed, especially during periods of high disease pressure. Prune plants to improve air circulation and reduce disease spread.*'
        },

    },
    'Potato': {
        'Early Blight': {
            'Description': '*Early blight is a fungal disease caused by the pathogen Alternaria solani that affects potato plants. It appears as dark, concentric rings with yellow halos on the leaves, starting from the lower leaves and progressing upward. The disease is favored by warm, humid conditions and can spread rapidly in dense plantings.*',
            'Symptoms': '*Dark, concentric rings with yellow halos on the leaves, starting from the lower leaves and progressing upward. Lesions may enlarge and coalesce, leading to widespread blighting of the foliage. Infected tubers may develop sunken, dark lesions with concentric rings on the skin.*',
            'Treatment': '*To control early blight, practice good sanitation by removing and destroying infected plant material. Apply fungicides as directed, especially during periods of high disease pressure. Proper crop rotation and planting disease-resistant varieties can also help reduce disease incidence.*'
        },
        'Late Blight': {
            'Description': '*Late blight is a devastating fungal disease caused by the pathogen Phytophthora infestans that affects potato plants. It appears as dark, water-soaked lesions on the leaves, stems, and tubers, often accompanied by a white, fuzzy growth on the undersides of the leaves. The disease thrives in cool, wet conditions and can spread rapidly during periods of high humidity.*',
            'Symptoms': '*Dark, water-soaked lesions on the leaves, stems, and tubers, often with a white, fuzzy growth on the undersides of the leaves. Lesions may rapidly expand and coalesce, leading to widespread blighting of the foliage and rotting of the tubers. Infected tubers may develop a foul odor and become soft and watery.*',
            'Treatment': '*To control late blight, practice good sanitation by removing and destroying infected plant material. Apply fungicides as directed, especially during periods of high disease pressure. Proper crop rotation, planting disease-resistant varieties, and avoiding overhead irrigation can also help reduce disease incidence.*'
        }

    },
    'Strawberry': {
        'Leaf Scorch': {
            'Description': '*Leaf scorch is a fungal disease that affects strawberry plants. It appears as brown, necrotic spots on the leaves, which may enlarge and coalesce over time. The disease is caused by various pathogens and can be exacerbated by environmental stressors such as drought or high temperatures.*',
            'Symptoms': '*Brown, necrotic spots on the leaves, often with irregular margins. Lesions may start as small spots and enlarge to cover large portions of the leaf surface. Severe infections can cause defoliation and weaken the plant.*',
            'Treatment': '*To control leaf scorch, remove and destroy infected plant material. Practice good sanitation by removing fallen leaves and debris from around the plants. Avoid overhead irrigation and water the plants at the base to reduce leaf wetness. Apply fungicides as directed, especially during periods of high disease pressure.*'
        },

    },
    'Tomato': {
        'Bacterial Spot': {
            'Description': '*Bacterial spot is a common bacterial disease affecting tomato plants. It is caused by the bacterium Xanthomonas campestris pv. vesicatoria and can cause significant damage to leaves, fruit, and stems. The disease is favored by warm, humid conditions and can spread rapidly during wet weather.*',
            'Symptoms': '*Symptoms of bacterial spot include small, water-soaked lesions on the leaves, which later turn brown and may have a yellow halo. Lesions on the fruit may appear as small, raised spots with a water-soaked appearance. Severe infections can cause defoliation and fruit loss.*',
            'Treatment': '*To control bacterial spot, practice good sanitation by removing and destroying infected plant material. Apply copper-based fungicides or bactericides as directed, especially during periods of high disease pressure. Prune plants to improve air circulation and reduce disease spread.*'
        },
        'Early Blight': {
            'Description': '*Early blight is a fungal disease caused by the pathogen Alternaria solani that affects tomato plants. It appears as dark, concentric rings with yellow halos on the leaves, starting from the lower leaves and progressing upward. The disease is favored by warm, humid conditions and can spread rapidly in dense plantings.*',
            'Symptoms': '*Dark, concentric rings with yellow halos on the leaves, starting from the lower leaves and progressing upward. Lesions may enlarge and coalesce, leading to widespread blighting of the foliage. Infected fruit may also develop sunken lesions with concentric rings on the skin.*',
            'Treatment': '*To control early blight, practice good sanitation by removing and destroying infected plant material. Apply fungicides as directed, especially during periods of high disease pressure. Proper crop rotation and planting disease-resistant varieties can also help reduce disease incidence.*'
        },
        'Late Blight': {
            'Description': '*Late blight is a devastating fungal disease caused by the pathogen Phytophthora infestans that affects tomato plants. It appears as dark, water-soaked lesions on the leaves, stems, and fruit, often accompanied by a white, fuzzy growth on the undersides of the leaves. The disease thrives in cool, wet conditions and can spread rapidly during periods of high humidity.*',
            'Symptoms': '*Dark, water-soaked lesions on the leaves, stems, and fruit, often with a white, fuzzy growth on the undersides of the leaves. Lesions may rapidly expand and coalesce, leading to widespread blighting of the foliage and rotting of the fruit. Infected fruit may develop a foul odor and become soft and watery.*',
            'Treatment': '*To control late blight, practice good sanitation by removing and destroying infected plant material. Apply fungicides as directed, especially during periods of high disease pressure. Proper crop rotation, planting disease-resistant varieties, and avoiding overhead irrigation can also help reduce disease incidence.*'
        }

    }
}
