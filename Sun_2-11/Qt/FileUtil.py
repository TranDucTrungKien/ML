import pickle
import os

class FileUtil:
    @staticmethod
    def save_model(model, filename: str) -> bool:
        """Lưu model sklearn xuống file."""
        try:
            # Tạo thư mục nếu chưa tồn tại
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, "wb") as f:
                pickle.dump(model, f)
            print(f"[INFO] Model saved successfully to {filename}")
            return True
        except Exception as e:
            print(f"[ERROR] Failed to save model: {e}")
            return False

    @staticmethod
    def load_model(filename: str):
        """Nạp lại model sklearn từ file."""
        try:
            with open(filename, "rb") as f:
                model = pickle.load(f)
            print(f"[INFO] Model loaded successfully from {filename}")
            return model
        except Exception as e:
            print(f"[ERROR] Failed to load model: {e}")
            return None
