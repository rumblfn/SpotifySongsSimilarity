import { useRef, useEffect, useState, MouseEvent, WheelEvent } from 'react';

export const Camera = () => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [context, setContext] = useState<CanvasRenderingContext2D | null>(null);
  const [cameraPosition, setCameraPosition] = useState({ x: 0, y: 0 });
  const [scale, setScale] = useState(1);
  const [isDragging, setIsDragging] = useState(false);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (canvas) {
      const ctx = canvas.getContext('2d');
      setContext(ctx);
    }
  }, []);

  useEffect(() => {
    if (context) {
      // Clear canvas
      context.clearRect(0, 0, context.canvas.width, context.canvas.height);

      // Draw something (for example, a square)
      context.fillStyle = 'blue';
      context.fillRect(100 + cameraPosition.x, 100 + cameraPosition.y, 50 * scale, 50 * scale);
    }
  }, [context, cameraPosition, scale]);

  const handleMouseDown = () => {
    setIsDragging(true);
  };

  const handleMouseUp = () => {
    setIsDragging(false);
  };

  const handleMouseMove = (e: MouseEvent) => {
    if (isDragging) {
      // Move camera with mouse movement
      const sensitivity = 0.5; // Adjust sensitivity as needed
      setCameraPosition((prevPosition) => ({
        x: prevPosition.x + e.movementX * sensitivity,
        y: prevPosition.y + e.movementY * sensitivity
      }));
    }
  };

  const handleWheel = (e: WheelEvent) => {
    // Zoom in/out with scroll wheel
    const zoomSpeed = 0.1; // Adjust zoom speed as needed
    const newScale = scale - e.deltaY * zoomSpeed;

    // Limit scale to a reasonable range (e.g., between 0.5 and 3)
    setScale(Math.max(0.5, Math.min(3, newScale)));
  };

  return (
    <canvas
      ref={canvasRef}
      width={window.innerWidth}
      height={window.innerHeight}
      onMouseDown={handleMouseDown}
      onMouseUp={handleMouseUp}
      onMouseMove={handleMouseMove}
      onWheel={handleWheel}
    />
  );
};