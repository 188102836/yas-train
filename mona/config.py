config = {
    "height": 32,
    "train_width": 384,
    "batch_size": 128,
    "epoch": 50,
    "print_per": 100,
    "save_per": 600,

    "train_size": 200000,
    "validate_size": 10000,

    "pretrain": False,
    "pretrain_name": "chs_all.pt",

    # Set according to your CPU
    "dataloader_workers": 1,
    # Generate data online for train/val
    "online_train": True,
    "online_val": True,

    # Select model type: Genshin or StarRail
    "model_type": "Genshin"
}
