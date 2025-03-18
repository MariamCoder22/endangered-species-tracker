from tensorflow.keras.preprocessing.image import ImageDataGenerator  # type: ignore

def augment_images(input_dir, output_dir):
    datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )
    
    generator = datagen.flow_from_directory(
        input_dir,
        target_size=(224, 224),
        batch_size=32,
        save_to_dir=output_dir,
        save_prefix='aug',
        save_format='jpg'
    )
    
    for _ in range(100):
        generator.next()