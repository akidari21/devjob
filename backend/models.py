from sqlalchemy import Column, BigInteger, SmallInteger, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, relationship

Base = declarative_base()

# DB 테이블

# 회원
class Member(Base):
  __tablename__ = 'member'
  
  id = Column(BigInteger, primary_key=True, autoincrement=True)
  email: Mapped[str]
  name = Column(String, nullable=False)
  created_at = Column(DateTime, nullable=False)
  updated_at = Column(DateTime, nullable=True)
  
  
# 프로필
class Profile(Base):
  __tablename__ = 'profile'
  
  id = Column(BigInteger, primary_key=True, autoincrement=True)
  m_id = Column(BigInteger, ForeignKey("member.id"))
  member = relationship("Member", backref="profiles")
  cat_1 = Column(String, nullable=False)
  title = Column(String, nullable=False)
  is_open = Column(String, nullable=False)
  created_at = Column(DateTime, nullable=False)
  updated_at = Column(DateTime, nullable=True)
  
  
# 카테고리 업종
class Category(Base):
  __tablename__ = 'category'
  
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  s_name = Column(String, nullable=False)
  created_at = Column(DateTime, nullable=False)
  updated_at = Column(DateTime, nullable=True)