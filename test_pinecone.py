#!/usr/bin/env python3
"""
Pinecone 연결 테스트 스크립트
각 방법을 순서대로 테스트합니다.
"""

import os
from dotenv import load_dotenv

load_dotenv()

def test_langchain_pinecone():
    """langchain-pinecone 패키지 테스트"""
    try:
        from langchain_pinecone import PineconeVectorStore
        print("✅ langchain-pinecone import 성공")
        return True
    except Exception as e:
        print(f"❌ langchain-pinecone import 실패: {e}")
        return False

def test_langchain_community():
    """langchain-community의 Pinecone 테스트"""
    try:
        from langchain_community.vectorstores import Pinecone
        print("✅ langchain-community Pinecone import 성공")
        return True
    except Exception as e:
        print(f"❌ langchain-community Pinecone import 실패: {e}")
        return False

def test_pinecone_client():
    """pinecone-client 직접 import 테스트"""
    try:
        import pinecone
        print(f"✅ pinecone import 성공 (버전: {pinecone.__version__ if hasattr(pinecone, '__version__') else 'unknown'})")
        return True
    except Exception as e:
        print(f"❌ pinecone import 실패: {e}")
        return False

def test_connection():
    """실제 Pinecone 연결 테스트"""
    try:
        from langchain_openai import OpenAIEmbeddings

        # langchain-pinecone 시도
        try:
            from langchain_pinecone import PineconeVectorStore
            embedding = OpenAIEmbeddings(model="text-embedding-3-large")
            index_name = "tax-markdown-index"
            database = PineconeVectorStore.from_existing_index(
                index_name=index_name,
                embedding=embedding
            )
            print("✅ langchain-pinecone으로 Pinecone 연결 성공")
            return True
        except:
            pass

        # langchain-community 시도
        try:
            from langchain_community.vectorstores import Pinecone
            embedding = OpenAIEmbeddings(model="text-embedding-3-large")
            index_name = "tax-markdown-index"
            database = Pinecone.from_existing_index(
                index_name=index_name,
                embedding=embedding
            )
            print("✅ langchain-community로 Pinecone 연결 성공")
            return True
        except Exception as e:
            print(f"❌ Pinecone 연결 실패: {e}")
            return False

    except Exception as e:
        print(f"❌ 테스트 중 오류: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Pinecone 호환성 테스트")
    print("=" * 50)

    print("\n1. 패키지 import 테스트:")
    test_pinecone_client()
    test_langchain_pinecone()
    test_langchain_community()

    print("\n2. 실제 연결 테스트:")
    if os.getenv("OPENAI_API_KEY") and os.getenv("PINECONE_API_KEY"):
        test_connection()
    else:
        print("⚠️  환경 변수가 설정되지 않아 연결 테스트를 건너뜁니다.")
        print("   OPENAI_API_KEY와 PINECONE_API_KEY를 .env 파일에 설정하세요.")

    print("\n" + "=" * 50)
    print("테스트 완료")
    print("=" * 50)